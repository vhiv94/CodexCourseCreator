"""Ch2/L2 — Read a Line from the Keyboard: input(), a prompt, and str.strip() on the line."""

from __future__ import annotations

import ast
import subprocess
import sys
from pathlib import Path

import pytest


def _course_root() -> Path:
    return Path(__file__).resolve().parents[1]


def _learner_entrypoint() -> Path:
    return _course_root() / "src" / "main.py"


@pytest.fixture
def main_script() -> Path:
    path = _learner_entrypoint()
    assert path.is_file(), (
        f"Create the lesson entrypoint at {path} so it can read one line with input()."
    )
    return path


def _run_with_stdin(script: Path, stdin: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(script)],
        cwd=_course_root(),
        input=stdin,
        capture_output=True,
        text=True,
        timeout=10,
    )


def _input_calls(tree: ast.AST) -> list[ast.Call]:
    return [
        node
        for node in ast.walk(tree)
        if isinstance(node, ast.Call)
        and isinstance(node.func, ast.Name)
        and node.func.id == "input"
    ]


def _uses_strip(tree: ast.AST) -> bool:
    for node in ast.walk(tree):
        if not isinstance(node, ast.Call):
            continue
        func = node.func
        if isinstance(func, ast.Attribute) and func.attr == "strip":
            return True
        # str.strip(value) — uncommon at this level but valid
        if (
            isinstance(func, ast.Attribute)
            and isinstance(func.value, ast.Name)
            and func.value.id == "str"
            and func.attr == "strip"
        ):
            return True
    return False


def test_output_shows_stripped_note_not_padding_secret(
    main_script: Path,
) -> None:
    """Spine project_step: prompt for one line, strip it, surface the cleaned text on stdout."""
    secret = "L2_STRIP_CHECK_xyz"
    padded = f"   {secret}    "
    completed = _run_with_stdin(main_script, padded + "\n")
    assert completed.returncode == 0, (
        f"Expected exit status 0; got {completed.returncode}. "
        f"stderr:\n{completed.stderr}"
    )

    out = completed.stdout.replace("\r\n", "\n")
    assert secret in out, (
        "Print (or otherwise reveal) the study note text after stripping, "
        f"so output contains the token {secret!r}."
    )
    assert padded not in out, (
        "After str.strip(), the note should not include the same leading/trailing "
        "padding you typed. Output still contained the full padded string."
    )


def test_main_source_calls_input_once_with_prompt_and_uses_strip(main_script: Path) -> None:
    """Spine concept: input() with a prompt, cleaned with strip()."""
    source = main_script.read_text(encoding="utf-8")
    try:
        tree = ast.parse(source)
    except SyntaxError as exc:  # pragma: no cover - learner-authored file
        pytest.fail(f"main.py must be valid Python: {exc}")

    calls = _input_calls(tree)
    assert len(calls) == 1, (
        "Read exactly **one** study note line for this lesson—use a single input(...) "
        f"call in main.py. Found {len(calls)} input(...) call(s)."
    )

    (call,) = calls
    assert call.args or call.keywords, (
        "Give the user a visible **prompt** inside input(...), "
        "so the terminal shows what to type (positional string or prompt=...)."
    )

    assert _uses_strip(tree), (
        "Clean the line with **strip()** before you use or print the note "
        "(for example: something.strip())."
    )


# Canonical runner (from python/fundamentals/):
#   uv run pytest Ch2/L2.py
