"""Ch1/L2 — Build a Simple Banner: string literals and concatenation shape multi-line output."""

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
        f"Create the lesson entrypoint at {path} so running it prints a short banner."
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


def test_running_program_prints_short_multiline_banner(main_script: Path) -> None:
    """Banner = several visible lines (L1 was exactly one line); still no user input."""
    completed = _run_entrypoint(main_script)
    assert completed.returncode == 0

    out = completed.stdout.replace("\r\n", "\n").rstrip("\n")
    lines = out.split("\n")

    assert 2 <= len(lines) <= 20, (
        "Show a short multi-part banner: use multiple lines of printed text "
        f"(more than L1’s single line), but keep it small. Got {len(lines)} line(s)."
    )

    for i, line in enumerate(lines, start=1):
        assert line.strip() != "", (
            f"Banner line {i} must contain visible characters, not only whitespace."
        )


# Canonical runner (from python/fundamentals/):
#   uv run pytest Ch1/L2.py
