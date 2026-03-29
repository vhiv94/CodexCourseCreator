"""Append-only lesson tests for python/data-structures.

Run one lesson block with:
uv run pytest main_test.py -m <lesson_selector>
"""

from __future__ import annotations

import copy
import importlib
from typing import Any

import pytest


@pytest.fixture(scope="module")
def learner_module() -> Any:
    return importlib.import_module("main")


def require_attr(module: Any, name: str) -> Any:
    assert hasattr(module, name), (
        f"Expected `main.{name}` to exist for this lesson contract."
    )
    return getattr(module, name)


@pytest.mark.lesson_ch1_l1
def test_ch1_l1_normalize_inventory_event_canonical_shape(learner_module: Any) -> None:
    normalize_inventory_event = require_attr(learner_module, "normalize_inventory_event")
    raw_event = {
        "sku": "  sku-42 ",
        "location": " A1 ",
        "delta": 5,
        "kind": "RECEIVE",
        "timestamp": "2026-03-28T10:00:00Z",
    }
    normalized = normalize_inventory_event(raw_event)

    assert set(normalized.keys()) == {"sku", "location", "delta", "kind", "timestamp"}
    assert normalized["sku"] == "SKU-42"
    assert normalized["location"] == "A1"
    assert normalized["delta"] == 5
    assert normalized["kind"] == "receive"


@pytest.mark.lesson_ch1_l2
def test_ch1_l2_normalize_event_stream_is_pure_and_filters_invalid(
    learner_module: Any,
) -> None:
    normalize_event_stream = require_attr(learner_module, "normalize_event_stream")
    source = [
        {"sku": "sku-1", "location": "A1", "delta": 3, "kind": "receive", "timestamp": "t1"},
        {"sku": "sku-1", "location": "A1", "delta": 0, "kind": "adjust", "timestamp": "t2"},
        {"sku": "sku-2", "location": "B2", "delta": -1, "kind": "pick", "timestamp": "t3"},
    ]
    source_before = copy.deepcopy(source)
    out = normalize_event_stream(source)

    assert source == source_before, "normalize_event_stream should not mutate input."
    assert isinstance(out, list)
    assert len(out) == 2
    assert all(event["delta"] != 0 for event in out)


@pytest.mark.lesson_ch1_l3
def test_ch1_l3_build_stock_index_nested_by_sku_and_location(learner_module: Any) -> None:
    build_stock_index = require_attr(learner_module, "build_stock_index")
    normalized_events = [
        {"sku": "SKU-1", "location": "A1", "delta": 5, "kind": "receive", "timestamp": "t1"},
        {"sku": "SKU-1", "location": "A1", "delta": -2, "kind": "pick", "timestamp": "t2"},
        {"sku": "SKU-2", "location": "B1", "delta": 4, "kind": "receive", "timestamp": "t3"},
    ]
    stock = build_stock_index(normalized_events)

    assert stock["SKU-1"]["A1"] == 3
    assert stock["SKU-2"]["B1"] == 4
    assert set(stock.keys()) == {"SKU-1", "SKU-2"}


@pytest.mark.lesson_ch2_l1
def test_ch2_l1_audit_stack_lifo_behavior(learner_module: Any) -> None:
    AuditStack = require_attr(learner_module, "AuditStack")
    stack = AuditStack()
    stack.push({"id": 1})
    stack.push({"id": 2})
    assert stack.peek()["id"] == 2
    assert stack.pop()["id"] == 2
    assert stack.pop()["id"] == 1
    assert len(stack) == 0


@pytest.mark.lesson_ch2_l1
def test_ch2_l1_audit_stack_empty_pop_raises(learner_module: Any) -> None:
    AuditStack = require_attr(learner_module, "AuditStack")
    stack = AuditStack()
    with pytest.raises(IndexError):
        stack.pop()


@pytest.mark.lesson_ch2_l2
def test_ch2_l2_replenishment_queue_fifo_behavior(learner_module: Any) -> None:
    ReplenishmentQueue = require_attr(learner_module, "ReplenishmentQueue")
    queue = ReplenishmentQueue()
    queue.enqueue("SKU-1")
    queue.enqueue("SKU-2")
    assert queue.peek() == "SKU-1"
    assert queue.dequeue() == "SKU-1"
    assert queue.dequeue() == "SKU-2"
    assert len(queue) == 0


@pytest.mark.lesson_ch2_l2
def test_ch2_l2_replenishment_queue_empty_dequeue_raises(learner_module: Any) -> None:
    ReplenishmentQueue = require_attr(learner_module, "ReplenishmentQueue")
    queue = ReplenishmentQueue()
    with pytest.raises(IndexError):
        queue.dequeue()


@pytest.mark.lesson_ch2_l3
def test_ch2_l3_intake_coordinator_routes_to_audit_and_restock(learner_module: Any) -> None:
    AuditStack = require_attr(learner_module, "AuditStack")
    ReplenishmentQueue = require_attr(learner_module, "ReplenishmentQueue")
    IntakeCoordinator = require_attr(learner_module, "IntakeCoordinator")

    stock = {"SKU-1": {"A1": 2}}
    coordinator = IntakeCoordinator(
        stock_index=stock,
        audit_stack=AuditStack(),
        replenishment_queue=ReplenishmentQueue(),
        reorder_point=2,
    )
    event = {"sku": "SKU-1", "location": "A1", "delta": -1, "kind": "pick", "timestamp": "t1"}
    result = coordinator.process_event(event)

    assert isinstance(result, dict)
    assert result["restock_enqueued"] is True
    assert coordinator.audit_stack.peek()["sku"] == "SKU-1"
    assert coordinator.replenishment_queue.peek() == "SKU-1"


@pytest.mark.lesson_ch3_l1
def test_ch3_l1_linked_list_ledger_append_and_iteration(learner_module: Any) -> None:
    LedgerNode = require_attr(learner_module, "LedgerNode")
    MovementLedgerLinkedList = require_attr(learner_module, "MovementLedgerLinkedList")

    node = LedgerNode({"sku": "SKU-1", "delta": 2})
    assert node.value["sku"] == "SKU-1"
    assert node.next is None

    ledger = MovementLedgerLinkedList()
    ledger.append({"sku": "SKU-1", "delta": 2})
    ledger.append({"sku": "SKU-2", "delta": -1})

    assert list(ledger) == [{"sku": "SKU-1", "delta": 2}, {"sku": "SKU-2", "delta": -1}]
    assert len(ledger) == 2


@pytest.mark.lesson_ch3_l2
def test_ch3_l2_linked_list_remove_first_preserves_invariants(learner_module: Any) -> None:
    MovementLedgerLinkedList = require_attr(learner_module, "MovementLedgerLinkedList")
    ledger = MovementLedgerLinkedList()
    ledger.append({"sku": "SKU-1", "delta": 2})
    ledger.append({"sku": "SKU-2", "delta": -1})
    ledger.append({"sku": "SKU-3", "delta": 4})

    removed = ledger.remove_first(lambda row: row["sku"] == "SKU-2")

    assert removed == {"sku": "SKU-2", "delta": -1}
    assert list(ledger) == [{"sku": "SKU-1", "delta": 2}, {"sku": "SKU-3", "delta": 4}]
    assert len(ledger) == 2


@pytest.mark.lesson_ch3_l3
def test_ch3_l3_summarize_movements_returns_totals_and_net(learner_module: Any) -> None:
    summarize_movements = require_attr(learner_module, "summarize_movements")
    rows = [
        {"sku": "SKU-1", "delta": 5},
        {"sku": "SKU-1", "delta": -2},
        {"sku": "SKU-2", "delta": 3},
    ]
    summary = summarize_movements(rows)

    assert summary["total_events"] == 3
    assert summary["net_delta"] == 6
    assert summary["by_sku"]["SKU-1"] == 3
    assert summary["by_sku"]["SKU-2"] == 3


@pytest.mark.lesson_ch4_l1
def test_ch4_l1_build_allocation_map_respects_available_stock(learner_module: Any) -> None:
    build_allocation_map = require_attr(learner_module, "build_allocation_map")
    orders = [{"order_id": "O1", "sku": "SKU-1", "qty": 4}]
    stock = {"SKU-1": {"A1": 2, "B1": 3}}
    allocation = build_allocation_map(orders, stock)

    assert "O1" in allocation
    total_allocated = sum(qty for _location, qty in allocation["O1"])
    assert total_allocated == 4
    assert all(location in {"A1", "B1"} for location, _ in allocation["O1"])


@pytest.mark.lesson_ch4_l2
def test_ch4_l2_enforce_constraints_filters_blocked_candidates(learner_module: Any) -> None:
    enforce_allocation_constraints = require_attr(
        learner_module, "enforce_allocation_constraints"
    )
    candidates = [
        {"sku": "SKU-1", "location": "A1"},
        {"sku": "SKU-2", "location": "B9"},
        {"sku": "SKU-X", "location": "A2"},
    ]
    filtered = enforce_allocation_constraints(
        candidates,
        blocked_locations={"B9"},
        restricted_skus={"SKU-X"},
    )

    assert filtered == [{"sku": "SKU-1", "location": "A1"}]


@pytest.mark.lesson_ch4_l3
def test_ch4_l3_plan_picking_waves_is_deterministic_and_bounded(learner_module: Any) -> None:
    plan_picking_waves = require_attr(learner_module, "plan_picking_waves")
    picks = [
        {"order_id": "O1"},
        {"order_id": "O2"},
        {"order_id": "O3"},
        {"order_id": "O4"},
    ]
    waves = plan_picking_waves(picks, max_wave_size=2)

    assert waves == [
        [{"order_id": "O1"}, {"order_id": "O2"}],
        [{"order_id": "O3"}, {"order_id": "O4"}],
    ]


@pytest.mark.lesson_ch5_l1
def test_ch5_l1_select_restock_top_k_uses_priority_order(learner_module: Any) -> None:
    select_restock_top_k = require_attr(learner_module, "select_restock_top_k")
    tasks = [
        {"sku": "SKU-A", "priority": 3},
        {"sku": "SKU-B", "priority": 9},
        {"sku": "SKU-C", "priority": 5},
    ]
    top = select_restock_top_k(tasks, k=2)

    assert [row["sku"] for row in top] == ["SKU-B", "SKU-C"]


@pytest.mark.lesson_ch5_l2
def test_ch5_l2_tie_breaking_is_stable_for_equal_priority(learner_module: Any) -> None:
    select_restock_top_k = require_attr(learner_module, "select_restock_top_k")
    tasks = [
        {"sku": "SKU-B", "priority": 8},
        {"sku": "SKU-A", "priority": 8},
        {"sku": "SKU-C", "priority": 8},
    ]
    top = select_restock_top_k(tasks, k=3)

    assert [row["sku"] for row in top] == ["SKU-A", "SKU-B", "SKU-C"]


@pytest.mark.lesson_ch5_l3
def test_ch5_l3_estimate_planning_cost_monotonic_growth(learner_module: Any) -> None:
    estimate_planning_cost = require_attr(learner_module, "estimate_planning_cost")
    small = estimate_planning_cost(n_orders=10, n_candidates=20)
    large = estimate_planning_cost(n_orders=20, n_candidates=40)

    assert isinstance(small["complexity_class"], str)
    assert large["operations_upper_bound"] > small["operations_upper_bound"]


@pytest.mark.lesson_ch6_l1
def test_ch6_l1_control_tower_process_batch_and_snapshot(learner_module: Any) -> None:
    InventoryControlTower = require_attr(learner_module, "InventoryControlTower")
    tower = InventoryControlTower(reorder_point=2)
    events = [
        {"sku": "SKU-1", "location": "A1", "delta": 4, "kind": "receive", "timestamp": "t1"},
        {"sku": "SKU-1", "location": "A1", "delta": -3, "kind": "pick", "timestamp": "t2"},
    ]
    result = tower.process_batch(events)
    snapshot = tower.snapshot()

    assert result["processed"] == 2
    assert snapshot["stock"]["SKU-1"]["A1"] == 1
    assert snapshot["pending_restock"] == ["SKU-1"]


@pytest.mark.lesson_ch6_l2
def test_ch6_l2_build_kpi_report_is_pure_summary(learner_module: Any) -> None:
    build_kpi_report = require_attr(learner_module, "build_kpi_report")
    snapshot = {
        "stock": {"SKU-1": {"A1": 0}, "SKU-2": {"B1": 4}},
        "pending_restock": ["SKU-1", "SKU-3"],
        "orders_requested": 10,
        "orders_fulfilled": 8,
    }
    before = copy.deepcopy(snapshot)
    report = build_kpi_report(snapshot)

    assert snapshot == before
    assert report["fill_rate"] == 0.8
    assert report["pending_restock_count"] == 2
    assert "SKU-1" in report["stockout_skus"]


@pytest.mark.lesson_ch6_l3
def test_ch6_l3_simulate_failure_recovery_reports_replay_success(learner_module: Any) -> None:
    simulate_failure_recovery = require_attr(learner_module, "simulate_failure_recovery")
    events = [
        {"sku": "SKU-1", "location": "A1", "delta": 5, "kind": "receive", "timestamp": "t1"},
        {"sku": "SKU-1", "location": "A1", "delta": -2, "kind": "pick", "timestamp": "t2"},
        {"sku": "SKU-1", "location": "A1", "delta": -1, "kind": "pick", "timestamp": "t3"},
    ]
    outcome = simulate_failure_recovery(events, fail_after=2)

    assert outcome["recovered"] is True
    assert outcome["processed_count"] == 3
    assert outcome["replay_count"] >= 2
