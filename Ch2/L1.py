"""Ch2/L1 — Remember Values with Variables: readable string constants for app title and log filename."""

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


_TITLE_NAME = re.compile(
    r"(title|banner|heading|label|welcome|caption|app_?name)",
    re.IGNORECASE,
)
_LOG_FILENAME_NAME = re.compile(
    r"(filename|filepath|file_name|file_path|logfile|log_file|study_log|default_log|"
    r"log_name|log_path)",
    re.IGNORECASE,
)
_FILENAME_LIKE_VALUE = re.compile(r"\.[A-Za-z0-9]{1,16}$")


@pytest.fixture
def main_script() -> Path:
    path = _learner_entrypoint()
    assert path.is_file(), (
        f"Create the lesson entrypoint at {path} with variables for title and log filename."
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


def _collect_string_constant_assigns(tree: ast.AST) -> list[tuple[str, str]]:
    """(identifier, string literal) pairs from simple `name = \"...\"` / AnnAssign."""

    pairs: list[tuple[str, str]] = []

    class Visitor(ast.NodeVisitor):
        def visit_Assign(self, node: ast.Assign) -> None:
            value = node.value
            if not isinstance(value, ast.Constant) or not isinstance(value.value, str):
                self.generic_visit(node)
                return
            text = value.value
            if not text.strip():
                self.generic_visit(node)
                return
            for target in node.targets:
                if isinstance(target, ast.Name):
                    pairs.append((target.id, text))
            self.generic_visit(node)

        def visit_AnnAssign(self, node: ast.AnnAssign) -> None:
            if node.value is None:
                self.generic_visit(node)
                return
            value = node.value
            if not isinstance(value, ast.Constant) or not isinstance(value.value, str):
                self.generic_visit(node)
                return
            text = value.value
            if not text.strip():
                self.generic_visit(node)
                return
            target = node.target
            if isinstance(target, ast.Name):
                pairs.append((target.id, text))
            self.generic_visit(node)

    Visitor().visit(tree)
    return pairs


def test_running_program_exits_successfully(main_script: Path) -> None:
    """Depends on Ch1/L3 surface: entry script still runs as a program."""
    completed = _run_entrypoint(main_script)
    assert completed.returncode == 0, (
        f"Expected exit status 0; got {completed.returncode}. "
        f"stderr:\n{completed.stderr}"
    )


def test_main_defines_distinct_title_and_log_filename_variables(main_script: Path) -> None:
    """Spine project_step: store app title and default log filename in variables (string literals)."""
    source = main_script.read_text(encoding="utf-8")
    try:
        tree = ast.parse(source)
    except SyntaxError as exc:  # pragma: no cover - learner-authored file
        pytest.fail(f"main.py must be valid Python so it can be analyzed: {exc}")

    assigns = _collect_string_constant_assigns(tree)
    assert assigns, (
        "Define at least one variable using a string literal assignment "
        "(for example name = \"...\") so the title and log filename have readable homes."
    )

    title_hits = [
        (name, val)
        for name, val in assigns
        if _TITLE_NAME.search(name) and not _FILENAME_LIKE_VALUE.search(val.strip())
    ]
    log_hits = [
        (name, val)
        for name, val in assigns
        if _LOG_FILENAME_NAME.search(name) and _FILENAME_LIKE_VALUE.search(val.strip())
    ]

    assert title_hits, (
        "Assign the **app title** (or banner text) to a variable whose name makes that clear—"
        "for example include words like title, banner, heading, label, welcome, caption, or app_name. "
        "Use a real human-readable title string, not a filename with an extension."
    )

    assert log_hits, (
        "Assign the **default log filename** to a variable whose name suggests a file or log path—"
        "for example filename, log_file, study_log, default_log, etc. "
        "Use a string that looks like a filename (it should end with an extension such as .txt or .log)."
    )

    title_names = {n for n, _ in title_hits}
    log_names = {n for n, _ in log_hits}
    assert title_names.isdisjoint(log_names), (
        "Use **two different variables**: one for the visible title and one for the log filename. "
        f"You reused the same identifier(s) for both roles: {sorted(title_names & log_names)!r}"
    )


# Canonical runner (from python/fundamentals/):
#   uv run pytest Ch2/L1.py
