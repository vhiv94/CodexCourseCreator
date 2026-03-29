#!/usr/bin/env python3
"""Repository validation for course authoring contracts.

Checks:
1) Schema validity for each course's `course/spine.*` and `course/progress.*`.
2) Exact parity between `course/spine.*` chapter/lesson titles and `CONTENTS.md`.
3) Test scoping via `test_glob` and `lesson_selector` contracts.
"""

from __future__ import annotations

import argparse
import glob
import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any

try:
    import yaml
except ImportError as exc:  # pragma: no cover - environment/setup error
    raise SystemExit(
        "Missing dependency: pyyaml. Install with `pip install pyyaml`."
    ) from exc

try:
    import jsonschema
except ImportError as exc:  # pragma: no cover - environment/setup error
    raise SystemExit(
        "Missing dependency: jsonschema. Install with `pip install jsonschema`."
    ) from exc


CHAPTER_HEADING_RE = re.compile(r"^###\s+(Ch[1-9][0-9]*):\s+(.+?)\s*$")
LESSON_LINE_RE = re.compile(r"^[0-9]+\.\s+(.+?)\s*$")
LESSON_ID_RE = re.compile(r"^(L[1-9][0-9]*)(?:[._-]|$)")
LESSON_SELECTOR_RE = re.compile(r"^lesson_ch[1-9][0-9]*_l[1-9][0-9]*$")


@dataclass
class ValidationResults:
    errors: list[str]
    warnings: list[str]

    def add_error(self, message: str) -> None:
        self.errors.append(message)

    def add_warning(self, message: str) -> None:
        self.warnings.append(message)

    @property
    def ok(self) -> bool:
        return not self.errors


def load_structured_file(path: Path) -> Any:
    if path.suffix == ".json":
        return json.loads(path.read_text(encoding="utf-8"))
    if path.suffix in {".yaml", ".yml"}:
        return yaml.safe_load(path.read_text(encoding="utf-8"))
    raise ValueError(f"Unsupported file type: {path}")


def find_course_roots(repo_root: Path) -> list[Path]:
    roots: set[Path] = set()
    for rel in ("**/course/spine.yaml", "**/course/spine.yml", "**/course/spine.json"):
        for spine_path in repo_root.glob(rel):
            roots.add(spine_path.parent.parent)
    return sorted(roots)


def parse_contents(contents_path: Path) -> tuple[list[dict[str, Any]], list[str]]:
    chapters: list[dict[str, Any]] = []
    local_errors: list[str] = []
    current: dict[str, Any] | None = None

    for raw_line in contents_path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line:
            continue

        chapter_match = CHAPTER_HEADING_RE.match(line)
        if chapter_match:
            current = {
                "dir": chapter_match.group(1),
                "title": chapter_match.group(2),
                "lessons": [],
            }
            chapters.append(current)
            continue

        lesson_match = LESSON_LINE_RE.match(line)
        if lesson_match:
            if current is None:
                local_errors.append(
                    f"{contents_path}: lesson line appears before first chapter heading: {line!r}"
                )
            else:
                current["lessons"].append(lesson_match.group(1))

    if not chapters:
        local_errors.append(f"{contents_path}: no chapter headings found")

    return chapters, local_errors


def normalize_rel_posix(path: Path, start: Path) -> str:
    return path.relative_to(start).as_posix()


def validate_schema(
    instance: Any, schema: dict[str, Any], logical_name: str, results: ValidationResults
) -> None:
    validator_cls = getattr(jsonschema, "Draft202012Validator", None)
    if validator_cls is None:
        validator_cls = getattr(jsonschema, "Draft7Validator", None)
    if validator_cls is None:
        validator_cls = jsonschema.validators.validator_for(schema)
    validator_cls.check_schema(schema)
    validator = validator_cls(schema)
    errors = sorted(validator.iter_errors(instance), key=lambda err: list(err.path))
    for error in errors:
        location = ".".join(str(part) for part in error.path) or "<root>"
        results.add_error(f"{logical_name}: schema error at {location}: {error.message}")


def check_spine_contents_parity(
    spine_data: dict[str, Any],
    contents_data: list[dict[str, Any]],
    course_root: Path,
    results: ValidationResults,
) -> None:
    spine_chapters = spine_data.get("chapters", [])
    if not isinstance(spine_chapters, list):
        return

    if len(spine_chapters) != len(contents_data):
        results.add_error(
            f"{course_root}: chapter count mismatch between spine ({len(spine_chapters)}) "
            f"and CONTENTS.md ({len(contents_data)})"
        )

    max_len = min(len(spine_chapters), len(contents_data))
    for index in range(max_len):
        s_ch = spine_chapters[index]
        c_ch = contents_data[index]
        s_dir = s_ch.get("dir")
        s_title = s_ch.get("title")
        c_dir = c_ch["dir"]
        c_title = c_ch["title"]

        if s_dir != c_dir or s_title != c_title:
            results.add_error(
                f"{course_root}: chapter #{index + 1} mismatch; "
                f"spine=({s_dir!r}, {s_title!r}) vs CONTENTS=({c_dir!r}, {c_title!r})"
            )

        s_lessons = s_ch.get("lessons", [])
        if not isinstance(s_lessons, list):
            continue
        s_titles = [lesson.get("title") for lesson in s_lessons]
        c_titles = c_ch["lessons"]

        if s_titles != c_titles:
            results.add_error(
                f"{course_root}: lesson title/order mismatch in {s_dir or c_dir}; "
                f"spine={s_titles!r} vs CONTENTS={c_titles!r}"
            )


def test_glob_statically_scoped(chapter_dir: str, lesson_id: str, test_glob: str) -> bool:
    normalized = test_glob.replace("\\", "/")
    required_prefix = f"{chapter_dir}/{lesson_id}"
    return required_prefix in normalized and not normalized.startswith("/")


def validate_test_glob_scope(
    chapter_dir: str, lesson_id: str, test_glob: str, course_root: Path, results: ValidationResults
) -> None:
    prefix = f"{chapter_dir}/{lesson_id}"
    if ".." in Path(test_glob).parts:
        results.add_error(
            f"{course_root}: test_glob for {chapter_dir}/{lesson_id} cannot contain parent traversal: {test_glob!r}"
        )
        return

    if not test_glob_statically_scoped(chapter_dir, lesson_id, test_glob):
        results.add_error(
            f"{course_root}: test_glob for {chapter_dir}/{lesson_id} must include '{prefix}' "
            f"to stay lesson-local; got {test_glob!r}"
        )
        return

    resolved_paths = [
        Path(match)
        for match in glob.glob((course_root / test_glob).as_posix(), recursive=True)
        if Path(match).is_file()
    ]

    if not resolved_paths:
        results.add_warning(
            f"{course_root}: test_glob for {chapter_dir}/{lesson_id} currently resolves to no files: {test_glob!r}"
        )
        return

    for resolved in resolved_paths:
        rel = normalize_rel_posix(resolved, course_root)
        if not rel.startswith(f"{chapter_dir}/"):
            results.add_error(
                f"{course_root}: {chapter_dir}/{lesson_id} test_glob matched file outside chapter: {rel!r}"
            )
            continue

        base_name = resolved.name
        lesson_id_match = LESSON_ID_RE.match(base_name)
        if lesson_id_match and lesson_id_match.group(1) != lesson_id:
            results.add_error(
                f"{course_root}: {chapter_dir}/{lesson_id} test_glob matched another lesson's file: {rel!r}"
            )
            continue

        if not base_name.startswith(f"{lesson_id}.") and not base_name.startswith(
            (f"{lesson_id}_", f"{lesson_id}-")
        ):
            results.add_warning(
                f"{course_root}: {chapter_dir}/{lesson_id} matched {rel!r}; "
                "filename does not start with lesson id. Verify this is intentionally lesson-local."
            )


def validate_main_test_selector(
    chapter_dir: str,
    lesson_id: str,
    lesson_selector: Any,
    seen_selectors: dict[str, str],
    course_root: Path,
    results: ValidationResults,
) -> None:
    lesson_ref = f"{chapter_dir}/{lesson_id}"
    if not isinstance(lesson_selector, str) or not lesson_selector.strip():
        results.add_error(
            f"{course_root}: {lesson_ref} uses test_glob 'main_test.py' but has no lesson_selector"
        )
        return

    if not LESSON_SELECTOR_RE.match(lesson_selector):
        results.add_error(
            f"{course_root}: {lesson_ref} lesson_selector must match "
            f"'lesson_ch<chapter>_l<lesson>'; got {lesson_selector!r}"
        )

    previous = seen_selectors.get(lesson_selector)
    if previous is not None and previous != lesson_ref:
        results.add_error(
            f"{course_root}: duplicate lesson_selector {lesson_selector!r} for "
            f"{lesson_ref} and {previous}"
        )
    else:
        seen_selectors[lesson_selector] = lesson_ref


def validate_course_root(
    course_root: Path,
    spine_schema: dict[str, Any],
    progress_schema: dict[str, Any],
    results: ValidationResults,
) -> None:
    course_dir = course_root / "course"
    contents_path = course_root / "CONTENTS.md"

    spine_path = None
    for candidate in ("spine.yaml", "spine.yml", "spine.json"):
        path = course_dir / candidate
        if path.exists():
            spine_path = path
            break

    if spine_path is None:
        results.add_error(f"{course_root}: missing course/spine.yaml|yml|json")
        return

    try:
        spine_data = load_structured_file(spine_path)
    except Exception as exc:  # pragma: no cover - parse failure branch
        results.add_error(f"{spine_path}: failed to parse ({exc})")
        return

    validate_schema(spine_data, spine_schema, str(spine_path), results)

    progress_path = None
    for candidate in ("progress.yaml", "progress.yml", "progress.json"):
        path = course_dir / candidate
        if path.exists():
            progress_path = path
            break

    if progress_path is None:
        results.add_warning(f"{course_root}: missing optional course/progress.yaml|yml|json")
    else:
        try:
            progress_data = load_structured_file(progress_path)
            validate_schema(progress_data, progress_schema, str(progress_path), results)
        except Exception as exc:  # pragma: no cover - parse failure branch
            results.add_error(f"{progress_path}: failed to parse ({exc})")

    if not contents_path.exists():
        results.add_warning(
            f"{course_root}: missing CONTENTS.md; skipping spine/CONTENTS parity for this root"
        )
        return

    parsed_contents, contents_errors = parse_contents(contents_path)
    for err in contents_errors:
        results.add_error(err)

    if isinstance(spine_data, dict):
        seen_selectors: dict[str, str] = {}
        uses_main_test = False
        check_spine_contents_parity(spine_data, parsed_contents, course_root, results)

        for chapter in spine_data.get("chapters", []):
            if not isinstance(chapter, dict):
                continue
            chapter_dir = chapter.get("dir")
            lessons = chapter.get("lessons", [])
            if not chapter_dir or not isinstance(lessons, list):
                continue
            for lesson in lessons:
                if not isinstance(lesson, dict):
                    continue
                lesson_id = lesson.get("id")
                test_glob = lesson.get("test_glob")
                if not lesson_id or not test_glob:
                    continue
                if test_glob == "main_test.py":
                    uses_main_test = True
                    validate_main_test_selector(
                        chapter_dir=chapter_dir,
                        lesson_id=lesson_id,
                        lesson_selector=lesson.get("lesson_selector"),
                        seen_selectors=seen_selectors,
                        course_root=course_root,
                        results=results,
                    )
                else:
                    results.add_warning(
                        f"{course_root}: {chapter_dir}/{lesson_id} uses legacy per-lesson test_glob "
                        f"{test_glob!r}; migrate to 'main_test.py' + lesson_selector when feasible."
                    )
                    validate_test_glob_scope(
                        chapter_dir=chapter_dir,
                        lesson_id=lesson_id,
                        test_glob=test_glob,
                        course_root=course_root,
                        results=results,
                    )
        if uses_main_test and not (course_root / "main_test.py").exists():
            results.add_warning(
                f"{course_root}: spine uses 'main_test.py' but the file does not exist yet."
            )


def run(repo_root: Path) -> int:
    results = ValidationResults(errors=[], warnings=[])

    spine_schema_path = repo_root / "course" / "spine.schema.json"
    progress_schema_path = repo_root / "course" / "progress.schema.json"
    if not spine_schema_path.exists():
        results.add_error(f"Missing schema file: {spine_schema_path}")
        return 1
    if not progress_schema_path.exists():
        results.add_error(f"Missing schema file: {progress_schema_path}")
        return 1

    spine_schema = json.loads(spine_schema_path.read_text(encoding="utf-8"))
    progress_schema = json.loads(progress_schema_path.read_text(encoding="utf-8"))

    course_roots = find_course_roots(repo_root)
    if not course_roots:
        results.add_error("No course roots found (expected at least one course/spine.*).")

    for course_root in course_roots:
        validate_course_root(
            course_root=course_root,
            spine_schema=spine_schema,
            progress_schema=progress_schema,
            results=results,
        )

    for warning in results.warnings:
        print(f"WARN: {warning}")
    for error in results.errors:
        print(f"ERROR: {error}")

    if results.ok:
        print(f"OK: validated {len(course_roots)} course root(s).")
        return 0

    print(f"FAILED: {len(results.errors)} error(s), {len(results.warnings)} warning(s).")
    return 1


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate course creator repository contracts.")
    parser.add_argument(
        "--repo-root",
        type=Path,
        default=Path(__file__).resolve().parents[1],
        help="Repository root to validate (defaults to script parent parent).",
    )
    args = parser.parse_args()
    return run(args.repo_root.resolve())


if __name__ == "__main__":
    raise SystemExit(main())
