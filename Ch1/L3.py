"""Ch1/L3 — Comment What Your Script Does: full-line comments document banner + study-log intent."""

from __future__ import annotations

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
        f"Create the lesson entrypoint at {path} with comments and the L2-style banner output."
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


def _full_line_comment_bodies(source: str) -> list[str]:
    bodies: list[str] = []
    for raw in source.splitlines():
        stripped = raw.strip()
        if not stripped.startswith("#"):
            continue
        body = stripped[1:].strip()
        if body:
            bodies.append(body)
    return bodies


def test_running_program_exits_successfully(main_script: Path) -> None:
    completed = _run_entrypoint(main_script)
    assert completed.returncode == 0, (
        f"Expected exit status 0; got {completed.returncode}. "
        f"stderr:\n{completed.stderr}"
    )


def test_running_program_prints_short_multiline_banner(
    main_script: Path,
) -> None:
    """Depends on Ch1/L2: banner behavior stays valid while adding comments."""
    completed = _run_entrypoint(main_script)
    assert completed.returncode == 0

    out = completed.stdout.replace("\r\n", "\n").rstrip("\n")
    lines = out.split("\n")

    assert 2 <= len(lines) <= 20, (
        "Keep the short multi-line banner from L2: multiple visible lines, not a huge block. "
        f"Got {len(lines)} line(s)."
    )

    for i, line in enumerate(lines, start=1):
        assert line.strip() != "", (
            f"Banner line {i} must contain visible characters, not only whitespace."
        )


def test_main_script_has_full_line_comments_about_banner_and_study_log(
    main_script: Path,
) -> None:
    """Spine project_step: comments explain the banner and future study-log purpose."""
    source = main_script.read_text(encoding="utf-8")
    bodies = _full_line_comment_bodies(source)
    assert len(bodies) >= 2, (
        "Add at least two full-line # comments (non-empty text after #). "
        "Use them to explain the printed banner and the script’s future role as a study log."
    )

    short = [b for b in bodies if len(b) < 8]
    assert not short, (
        "Each full-line # comment should carry a short explanation, not a tiny placeholder. "
        f"Too-short comment body(ies): {short!r}"
    )

    blob = "\n".join(bodies)
    mentions_banner = re.search(
        r"banner|welcome|title|message|display|output|\bprint\b",
        blob,
        re.IGNORECASE,
    )
    assert mentions_banner is not None, (
        "At least one full-line # comment should explain what the printed banner/output is for, "
        "using plain words (for example: banner, welcome, what you print, display, output)."
    )

    mentions_log = re.search(r"\bstudy\b|\blog\b|notes?", blob, re.IGNORECASE)
    assert mentions_log is not None, (
        "At least one full-line # comment should mention the future study-log direction "
        "(for example: study, log, notes)—even if that behavior is not built yet."
    )


# Canonical runner (from python/fundamentals/):
#   uv run pytest Ch1/L3.py
