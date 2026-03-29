#!/usr/bin/env python3
"""Guard against accidental test coverage regressions in CI.

Checks:
1) Legacy per-lesson test files (Ch#/L#.py) are not deleted.
2) Existing lesson selectors are not removed from main_test*.py files.
3) Existing spine lesson selectors are not changed for already-defined lessons.
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path
from typing import Any

try:
    import yaml
except ImportError as exc:  # pragma: no cover - environment/setup error
    raise SystemExit(
        "Missing dependency: pyyaml. Install with `pip install pyyaml`."
    ) from exc


LEGACY_TEST_FILE_RE = re.compile(r"(^|.*/)Ch[1-9][0-9]*/L[1-9][0-9]*\.py$")
MAIN_TEST_FILE_RE = re.compile(r"(^|.*/)main_test(?:_[a-z0-9_]+)?\.py$")
SELECTOR_RE = re.compile(r"\blesson_ch[1-9][0-9]*_l[1-9][0-9]*\b")
SPINE_FILE_RE = re.compile(r"(^|.*/)course/spine\.(?:yaml|yml|json)$")


def run_git(repo_root: Path, args: list[str]) -> tuple[int, str, str]:
    proc = subprocess.run(
        ["git", *args],
        cwd=repo_root,
        text=True,
        capture_output=True,
        check=False,
    )
    return proc.returncode, proc.stdout, proc.stderr


def resolve_base_ref(repo_root: Path, explicit: str | None) -> str | None:
    candidates = [explicit, "origin/main", "origin/master", "HEAD~1"]
    for candidate in candidates:
        if not candidate:
            continue
        rc, _, _ = run_git(repo_root, ["rev-parse", "--verify", candidate])
        if rc == 0:
            return candidate
    return None


def get_changed_rows(repo_root: Path, base_ref: str) -> list[str]:
    rc, out, err = run_git(
        repo_root,
        ["diff", "--name-status", f"{base_ref}...HEAD"],
    )
    if rc != 0:
        raise RuntimeError(f"Failed to read git diff: {err.strip() or out.strip()}")
    rows = [line.strip() for line in out.splitlines() if line.strip()]
    return rows


def get_file_from_ref(repo_root: Path, ref: str, rel_path: str) -> str | None:
    rc, out, _ = run_git(repo_root, ["show", f"{ref}:{rel_path}"])
    if rc != 0:
        return None
    return out


def parse_spine_text(path: str, text: str) -> dict[str, Any] | None:
    suffix = Path(path).suffix.lower()
    if suffix == ".json":
        loaded = json.loads(text)
    else:
        loaded = yaml.safe_load(text)
    return loaded if isinstance(loaded, dict) else None


def collect_spine_lessons_from_ref(
    repo_root: Path, ref: str
) -> dict[tuple[str, str, str], dict[str, str]]:
    rc, out, err = run_git(repo_root, ["ls-tree", "-r", "--name-only", ref])
    if rc != 0:
        raise RuntimeError(f"Failed listing files for {ref}: {err.strip() or out.strip()}")

    lesson_map: dict[tuple[str, str, str], dict[str, str]] = {}
    for rel_path in out.splitlines():
        if not SPINE_FILE_RE.search(rel_path):
            continue
        text = get_file_from_ref(repo_root, ref, rel_path)
        if text is None:
            continue
        spine = parse_spine_text(rel_path, text)
        if spine is None:
            continue

        course_root = str(Path(rel_path).parent.parent).replace("\\", "/")
        chapters = spine.get("chapters", [])
        if not isinstance(chapters, list):
            continue

        for chapter in chapters:
            if not isinstance(chapter, dict):
                continue
            chapter_dir = chapter.get("dir")
            lessons = chapter.get("lessons", [])
            if not isinstance(chapter_dir, str) or not isinstance(lessons, list):
                continue
            for lesson in lessons:
                if not isinstance(lesson, dict):
                    continue
                lesson_id = lesson.get("id")
                test_glob = lesson.get("test_glob")
                lesson_selector = lesson.get("lesson_selector")
                if not isinstance(lesson_id, str):
                    continue
                lesson_map[(course_root, chapter_dir, lesson_id)] = {
                    "test_glob": test_glob if isinstance(test_glob, str) else "",
                    "lesson_selector": lesson_selector
                    if isinstance(lesson_selector, str)
                    else "",
                }
    return lesson_map


def parse_name_status_row(row: str) -> tuple[str, list[str]]:
    parts = row.split("\t")
    status = parts[0]
    return status, parts[1:]


def find_removed_selectors(base_text: str, head_text: str) -> set[str]:
    base_selectors = set(SELECTOR_RE.findall(base_text))
    head_selectors = set(SELECTOR_RE.findall(head_text))
    return base_selectors - head_selectors


def run(repo_root: Path, base_ref_arg: str | None) -> int:
    rc, _, _ = run_git(repo_root, ["rev-parse", "--is-inside-work-tree"])
    if rc != 0:
        print("SKIP: Not a git repository; test regression check skipped.")
        return 0

    base_ref = resolve_base_ref(repo_root, base_ref_arg)
    if base_ref is None:
        print("ERROR: Could not resolve a git base ref for comparison.")
        return 1

    try:
        changed_rows = get_changed_rows(repo_root, base_ref)
    except RuntimeError as exc:
        print(f"ERROR: {exc}")
        return 1

    errors: list[str] = []

    for row in changed_rows:
        status, paths = parse_name_status_row(row)
        if status.startswith("D") and paths:
            deleted_path = paths[0]
            if LEGACY_TEST_FILE_RE.search(deleted_path):
                errors.append(
                    f"Deleted legacy lesson test file detected: {deleted_path}. "
                    "Do not remove prior lesson tests in migration/lesson PRs."
                )

    touched_main_tests: set[str] = set()
    for row in changed_rows:
        status, paths = parse_name_status_row(row)
        if not paths:
            continue
        candidate_paths = paths if status.startswith("R") else [paths[0]]
        for rel_path in candidate_paths:
            if MAIN_TEST_FILE_RE.search(rel_path):
                touched_main_tests.add(rel_path)

    for rel_path in sorted(touched_main_tests):
        base_text = get_file_from_ref(repo_root, base_ref, rel_path)
        head_text = (repo_root / rel_path).read_text(encoding="utf-8") if (repo_root / rel_path).exists() else ""
        if base_text is None:
            continue
        removed = find_removed_selectors(base_text=base_text, head_text=head_text)
        if removed:
            errors.append(
                f"{rel_path}: removed existing lesson selector(s): {', '.join(sorted(removed))}. "
                "Prior lesson selector blocks must stay intact."
            )

    try:
        base_lessons = collect_spine_lessons_from_ref(repo_root, base_ref)
        head_lessons = collect_spine_lessons_from_ref(repo_root, "HEAD")
    except RuntimeError as exc:
        print(f"ERROR: {exc}")
        return 1

    for lesson_ref, base_fields in base_lessons.items():
        if lesson_ref not in head_lessons:
            continue
        head_fields = head_lessons[lesson_ref]
        if base_fields["lesson_selector"] and (
            base_fields["lesson_selector"] != head_fields["lesson_selector"]
        ):
            course_root, chapter_dir, lesson_id = lesson_ref
            errors.append(
                f"{course_root} {chapter_dir}/{lesson_id}: lesson_selector changed "
                f"from {base_fields['lesson_selector']!r} to {head_fields['lesson_selector']!r}. "
                "Do not rewrite prior lesson selector contracts."
            )

    if errors:
        for err in errors:
            print(f"ERROR: {err}")
        print(f"FAILED: {len(errors)} regression error(s).")
        return 1

    print("OK: no prior-lesson test regressions detected.")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Detect accidental prior-lesson test regressions using git history."
    )
    parser.add_argument(
        "--repo-root",
        type=Path,
        default=Path(__file__).resolve().parents[1],
        help="Repository root to validate (defaults to script parent parent).",
    )
    parser.add_argument(
        "--base-ref",
        type=str,
        default=None,
        help="Git base ref/sha to compare against (default: origin/main, origin/master, or HEAD~1).",
    )
    args = parser.parse_args()
    return run(args.repo_root.resolve(), args.base_ref)


if __name__ == "__main__":
    raise SystemExit(main())
