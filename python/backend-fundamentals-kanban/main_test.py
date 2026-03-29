from __future__ import annotations

import importlib
import sqlite3
from pathlib import Path
from typing import Any

import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient


def _resolve_app(module: Any) -> FastAPI:
    app = getattr(module, "app", None)
    if app is None and hasattr(module, "create_app"):
        app = module.create_app()

    assert app is not None, "Expose a FastAPI app as `app` or `create_app()` in main.py."
    assert isinstance(app, FastAPI), "Resolved application must be a FastAPI instance."
    return app


def _json(response):
    try:
        return response.json()
    except Exception as exc:  # pragma: no cover - failure path clarity
        pytest.fail(f"Expected JSON response, got parse error: {exc}", pytrace=False)


def _assert_json_content_type(response) -> None:
    content_type = response.headers.get("content-type", "")
    assert "application/json" in content_type.lower(), (
        f"Expected JSON content-type, got: {content_type!r}"
    )


def _assert_error_envelope(response, expected_statuses: set[int]) -> dict[str, Any]:
    assert response.status_code in expected_statuses, (
        f"Expected one of {sorted(expected_statuses)}, got {response.status_code}."
    )
    _assert_json_content_type(response)
    payload = _json(response)
    assert isinstance(payload, dict), "Error responses should be JSON objects."

    has_detail = "detail" in payload
    has_error = "error" in payload
    assert has_detail or has_error, "Error response should include `detail` or `error`."

    if has_error:
        error = payload["error"]
        assert isinstance(error, (dict, str)), "`error` should be a string or object."
        if isinstance(error, dict):
            assert {"code", "message"} <= set(error.keys()) or "message" in error, (
                "Object `error` should include a message and preferably a code."
            )
    return payload


@pytest.fixture
def db_path(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> Path:
    path = tmp_path / "kanban_ch1.db"
    monkeypatch.setenv("KANBAN_DB_PATH", str(path))
    return path


@pytest.fixture
def app_module(db_path: Path):
    module = importlib.import_module("main")
    return importlib.reload(module)


@pytest.fixture
def client(app_module) -> TestClient:
    return TestClient(_resolve_app(app_module))


def _extract_id(payload: dict[str, Any]) -> Any:
    for key in ("id", "board_id", "column_id", "task_id"):
        if key in payload:
            return payload[key]
    pytest.fail(f"Expected one of id/board_id/column_id/task_id keys, got: {payload}")


def _create_board(client: TestClient, name: str = "Planning Board") -> dict[str, Any]:
    response = client.post("/boards", json={"name": name})
    assert response.status_code in {200, 201}, (
        "POST /boards should create a board and return 200 or 201."
    )
    _assert_json_content_type(response)
    payload = _json(response)
    assert isinstance(payload, dict), "POST /boards should return a JSON object."
    assert any(k in payload for k in ("id", "board_id")), (
        "Created board response should expose a stable identifier."
    )
    return payload


class TestLessonCh1L1WhatIsAServer:
    pytestmark = pytest.mark.lesson_ch1_l1

    def test_app_bootstrap_exposes_fastapi_instance(self, app_module):
        _resolve_app(app_module)

    def test_health_endpoint_is_reachable(self, client: TestClient):
        response = client.get("/health")
        assert response.status_code == 200, "GET /health should return 200."

    def test_health_endpoint_returns_deterministic_status_field(self, client: TestClient):
        payload = _json(client.get("/health"))
        assert isinstance(payload, dict), "Health payload should be a JSON object."
        assert "status" in payload, "Health payload should include a `status` field."
        assert str(payload["status"]).lower() in {"ok", "healthy", "up"}

    def test_health_endpoint_uses_json_content_type(self, client: TestClient):
        response = client.get("/health")
        _assert_json_content_type(response)

    def test_health_rejects_post_requests(self, client: TestClient):
        response = client.post("/health", json={})
        assert response.status_code == 405, "POST /health should be method-not-allowed."

    def test_unknown_route_returns_not_found_error(self, client: TestClient):
        response = client.get("/no-such-route")
        _assert_error_envelope(response, {404})


class TestLessonCh1L2HttpRequestResponseContract:
    pytestmark = pytest.mark.lesson_ch1_l2

    def test_create_board_accepts_json_body(self, client: TestClient):
        payload = _create_board(client, name="Sprint 1")
        assert payload.get("name") == "Sprint 1"

    def test_create_board_uses_json_content_type(self, client: TestClient):
        response = client.post("/boards", json={"name": "Contract Board"})
        assert response.status_code in {200, 201}
        _assert_json_content_type(response)

    def test_list_boards_returns_json_array(self, client: TestClient):
        _create_board(client, name="Listable Board")
        response = client.get("/boards")
        assert response.status_code == 200, "GET /boards should return 200."
        _assert_json_content_type(response)
        payload = _json(response)
        assert isinstance(payload, list), "GET /boards should return a JSON list."

    def test_create_board_rejects_missing_required_name(self, client: TestClient):
        response = client.post("/boards", json={})
        _assert_error_envelope(response, {400, 422})

    def test_create_board_rejects_wrong_name_type(self, client: TestClient):
        response = client.post("/boards", json={"name": 123})
        _assert_error_envelope(response, {400, 422})

    def test_boards_route_rejects_patch_method(self, client: TestClient):
        response = client.patch("/boards", json={"name": "Nope"})
        _assert_error_envelope(response, {405})


class TestLessonCh1L3RoutingAndResourceModeling:
    pytestmark = pytest.mark.lesson_ch1_l3

    def test_columns_are_nested_under_board_resources(self, client: TestClient):
        board = _create_board(client, name="Nested Board")
        board_id = _extract_id(board)
        response = client.post(f"/boards/{board_id}/columns", json={"name": "Todo"})
        assert response.status_code in {200, 201}, (
            "POST /boards/{board_id}/columns should create a column."
        )

    def test_tasks_can_be_created_under_board_and_column(self, client: TestClient):
        board = _create_board(client, name="Task Board")
        board_id = _extract_id(board)
        column_res = client.post(f"/boards/{board_id}/columns", json={"name": "Doing"})
        assert column_res.status_code in {200, 201}
        column = _json(column_res)
        column_id = _extract_id(column)

        response = client.post(
            f"/boards/{board_id}/columns/{column_id}/tasks",
            json={"title": "Ship Ch1"},
        )
        assert response.status_code in {200, 201}, (
            "POST /boards/{board_id}/columns/{column_id}/tasks should create a task."
        )

    def test_unknown_board_route_returns_not_found(self, client: TestClient):
        response = client.get("/boards/does-not-exist")
        _assert_error_envelope(response, {404})

    def test_unknown_column_under_valid_board_returns_not_found(self, client: TestClient):
        board = _create_board(client, name="Parent Board")
        board_id = _extract_id(board)
        response = client.get(f"/boards/{board_id}/columns/missing-column")
        _assert_error_envelope(response, {404})

    def test_parent_child_mismatch_is_rejected(self, client: TestClient):
        board_a = _create_board(client, name="A")
        board_b = _create_board(client, name="B")
        board_a_id = _extract_id(board_a)
        board_b_id = _extract_id(board_b)

        column_res = client.post(f"/boards/{board_a_id}/columns", json={"name": "Only A"})
        assert column_res.status_code in {200, 201}
        column_id = _extract_id(_json(column_res))

        response = client.post(
            f"/boards/{board_b_id}/columns/{column_id}/tasks",
            json={"title": "Wrong Parent"},
        )
        _assert_error_envelope(response, {400, 404, 409})

    def test_successful_write_creates_sqlite_file(self, client: TestClient, db_path: Path):
        _create_board(client, name="SQLite Check")
        assert db_path.exists(), (
            "Creating data in Chapter 1 should initialize a SQLite-backed datastore."
        )
        with sqlite3.connect(db_path) as connection:
            cursor = connection.execute("PRAGMA schema_version;")
            row = cursor.fetchone()
        assert row is not None, "SQLite database should be queryable after write operations."


class TestLessonCh1L4ApiDesignMethodsStatusAndErrors:
    pytestmark = pytest.mark.lesson_ch1_l4

    def test_create_board_uses_create_semantic_status(self, client: TestClient):
        response = client.post("/boards", json={"name": "Semantic Status"})
        assert response.status_code in {200, 201}, (
            "Create operations should use a success status (prefer 201)."
        )

    def test_board_not_found_uses_404(self, client: TestClient):
        response = client.get("/boards/unknown-board")
        _assert_error_envelope(response, {404})

    def test_validation_error_uses_400_or_422(self, client: TestClient):
        response = client.post("/boards", json={"name": ""})
        _assert_error_envelope(response, {400, 422})

    def test_method_not_allowed_uses_405(self, client: TestClient):
        response = client.put("/boards", json={"name": "No Put"})
        _assert_error_envelope(response, {405})

    def test_error_shape_is_consistent_across_common_failures(self, client: TestClient):
        validation_payload = _assert_error_envelope(
            client.post("/boards", json={}), {400, 422}
        )
        not_found_payload = _assert_error_envelope(client.get("/boards/missing"), {404})

        validation_keys = set(validation_payload.keys())
        not_found_keys = set(not_found_payload.keys())
        assert validation_keys & not_found_keys, (
            "Error payloads should share at least one stable top-level key for consistency."
        )

    def test_error_payload_fields_are_json_serializable(self, client: TestClient):
        response = client.get("/boards/missing-again")
        payload = _assert_error_envelope(response, {404})
        assert isinstance(payload, dict), "Error payload should be an object for API clients."
