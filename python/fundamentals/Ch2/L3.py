"""Ch2/L3 — Choose What Happens Next: if / else and rejecting empty stripped input."""

from __future__ import annotations

import ast
import re
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
        f"Create the lesson entrypoint at {path} so it can validate one stripped note line."
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
        if (
            isinstance(func, ast.Attribute)
            and isinstance(func.value, ast.Name)
            and func.value.id == "str"
            and func.attr == "strip"
        ):
            return True
    return False


def _has_if_with_branching_else(tree: ast.AST) -> bool:
    for node in ast.walk(tree):
        if isinstance(node, ast.If) and node.orelse:
            return True
    return False


# Avoid words that commonly appear in input() prompts (e.g. "Enter …", "Type …").
_REJECTION_HINT = re.compile(
    r"\b(empty|emptied|missing|nothing|invalid|reject|retry)\b|"
    r"(try again|no note|blank line|can't use|cannot use|not accepted)",
    re.IGNORECASE,
)


def test_non_empty_stripped_note_still_surfaces(main_script: Path) -> None:
    """Builds on Ch2/L2: valid notes still reach stdout trimmed (same padding contract)."""
    secret = "L3_OK_NOTE_abc"
    padded = f"   {secret}    "
    completed = _run_with_stdin(main_script, padded + "\n")
    assert completed.returncode == 0, (
        f"Expected exit status 0; got {completed.returncode}. "
        f"stderr:\n{completed.stderr}"
    )

    out = completed.stdout.replace("\r\n", "\n")
    assert secret in out, (
        "When the stripped note has text, show that text on stdout—"
        f"tests expect to find {secret!r} in the captured output."
    )
    assert padded not in out, (
        "Do not print the raw padded input; strip before you display the note."
    )


def test_whitespace_only_line_triggers_rejection_message(main_script: Path) -> None:
    """Spine project_step: empty-after-strip must not follow the happy-path note echo."""
    completed = _run_with_stdin(main_script, " \t  \n")
    assert completed.returncode == 0, (
        f"Expected exit status 0; got {completed.returncode}. "
        f"stderr:\n{completed.stderr}"
    )
    out = completed.stdout.replace("\r\n", "\n")
    assert _REJECTION_HINT.search(out), (
        "After strip, an all-blank line becomes empty—tell the user clearly (stdout) that "
        "the note was rejected, empty, missing, etc. Use readable words; see this test's pattern."
    )


def test_main_uses_if_else_branch_strip_and_single_input(main_script: Path) -> None:
    """Spine concept: if / else plus input + strip (exactly one read, like L2)."""
    source = main_script.read_text(encoding="utf-8")
    try:
        tree = ast.parse(source)
    except SyntaxError as exc:  # pragma: no cover - learner-authored file
        pytest.fail(f"main.py must be valid Python: {exc}")

    assert _has_if_with_branching_else(tree), (
        "Model the two outcomes with **if / else** (or if + elif chain): one branch handles "
        "the empty-after-strip case and the other handles a real note."
    )

    calls = _input_calls(tree)
    assert len(calls) == 1, (
        "Still read exactly **one** line with input(...) for this lesson. "
        f"Found {len(calls)} input(...) call(s)."
    )

    (call,) = calls
    assert call.args or call.keywords, (
        "Keep a visible prompt argument on input(...) so users know what to type."
    )

    assert _uses_strip(tree), (
        "Continue stripping the line (for example with .strip()) before checking emptiness."
    )


# Canonical runner (from python/fundamentals/):
#   uv run pytest Ch2/L3.py
