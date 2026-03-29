"""Ch1/L1 — Hello from Python: running a script prints a one-line welcome."""

from __future__ import annotations

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
        f"Create the lesson entrypoint at {path} so running it prints one welcome line."
    )
    return path


def _run_entrypoint(script: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(script)],
        cwd=_course_root(),
        capture_output=True,
        text=True,
        timeout=10,
    )


def test_running_program_exits_successfully(main_script: Path) -> None:
    completed = _run_entrypoint(main_script)
    assert completed.returncode == 0, (
        f"Expected exit status 0; got {completed.returncode}. "
        f"stderr:\n{completed.stderr}"
    )


def test_running_program_prints_one_non_empty_welcome_line(main_script: Path) -> None:
    completed = _run_entrypoint(main_script)
    assert completed.returncode == 0

    # Normalize newlines; allow single trailing newline from print.
    out = completed.stdout.replace("\r\n", "\n").rstrip("\n")
    lines = out.split("\n")
    assert len(lines) == 1, (
        "Print exactly one line of welcome text (one print or one line). "
        f"Got {len(lines)} line(s): {lines!r}"
    )
    assert lines[0].strip() != "", "The welcome line must contain visible text, not only whitespace."


# Canonical runner (from python/fundamentals/):
#   uv run pytest Ch1/L1.py
