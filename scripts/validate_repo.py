#!/usr/bin/env python3
"""Repository validation for course authoring contracts.

Checks:
1) Schema validity for each course's `course/spine.*` and `course/progress.*`.
2) Exact parity between `course/spine.*` and `CONTENTS.md`, including module headings.
3) Test scoping via `test_glob` and `lesson_selector` contracts.
4) Cross-reference validation for dependencies and adaptive progress targets.
"""

from __future__ import annotations

import argparse
import glob
import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterator

try:
    import yaml
except ImportError as exc:  # pragma: no cover - environment/setup error
    raise SystemExit("Missing dependency: pyyaml. Install with `pip install pyyaml`.") from exc

try:
    import jsonschema
except ImportError as exc:  # pragma: no cover - environment/setup error
    raise SystemExit(
        "Missing dependency: jsonschema. Install with `pip install jsonschema`."
    ) from exc


MODULE_HEADING_RE = re.compile(r"^##\s+(M[1-9][0-9]*):\s+(.+?)\s*$")
CHAPTER_HEADING_RE = re.compile(r"^###\s+(Ch[1-9][0-9]*):\s+(.+?)\s*$")
LESSON_LINE_RE = re.compile(r"^[0-9]+\.\s+(.+?)\s*$")
LESSON_ID_RE = re.compile(r"^(L[1-9][0-9]*)(?:[._-]|$)")
LESSON_SELECTOR_RE = re.compile(r"^lesson_ch([1-9][0-9]*)_l([1-9][0-9]*)$")
MAIN_TEST_GLOB_RE = re.compile(r"^main_test(?:_[a-z0-9_]+)?\.py$")


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


@dataclass
class CourseRefs:
    module_ids: set[str]
    chapter_dirs: set[str]
    lesson_refs: set[str]
    lesson_order: dict[str, int]


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


def normalize_rel_posix(path: Path, start: Path) -> str:
    return path.relative_to(start).as_posix()


def get_spine_modules(spine_data: dict[str, Any]) -> tuple[bool, list[dict[str, Any]]]:
    modules = spine_data.get("modules")
    if isinstance(modules, list):
        return True, modules

    chapters = spine_data.get("chapters", [])
    if isinstance(chapters, list):
        return False, [{"id": None, "title": None, "chapters": chapters}]

    return False, []


def iter_spine_chapters(spine_data: dict[str, Any]) -> Iterator[tuple[str | None, dict[str, Any]]]:
    _, modules = get_spine_modules(spine_data)
    for module in modules:
        module_id = module.get("id") if isinstance(module, dict) else None
        chapters = module.get("chapters", []) if isinstance(module, dict) else []
        if not isinstance(chapters, list):
            continue
        for chapter in chapters:
            if isinstance(chapter, dict):
                yield module_id, chapter


def iter_spine_lessons(
    spine_data: dict[str, Any],
) -> Iterator[tuple[str | None, str, dict[str, Any]]]:
    for module_id, chapter in iter_spine_chapters(spine_data):
        chapter_dir = chapter.get("dir")
        lessons = chapter.get("lessons", [])
        if not isinstance(chapter_dir, str) or not isinstance(lessons, list):
            continue
        for lesson in lessons:
            if isinstance(lesson, dict):
                yield module_id, chapter_dir, lesson


def collect_course_refs(spine_data: dict[str, Any]) -> CourseRefs:
    module_ids: set[str] = set()
    chapter_dirs: set[str] = set()
    lesson_refs: set[str] = set()
    lesson_order: dict[str, int] = {}

    order = 0
    for module_id, chapter in iter_spine_chapters(spine_data):
        if isinstance(module_id, str):
            module_ids.add(module_id)
        chapter_dir = chapter.get("dir")
        lessons = chapter.get("lessons", [])
        if not isinstance(chapter_dir, str) or not isinstance(lessons, list):
            continue
        chapter_dirs.add(chapter_dir)
        for lesson in lessons:
            if not isinstance(lesson, dict):
                continue
            lesson_id = lesson.get("id")
            if not isinstance(lesson_id, str):
                continue
            lesson_ref = f"{chapter_dir}/{lesson_id}"
            lesson_refs.add(lesson_ref)
            lesson_order[lesson_ref] = order
            order += 1

    return CourseRefs(
        module_ids=module_ids,
        chapter_dirs=chapter_dirs,
        lesson_refs=lesson_refs,
        lesson_order=lesson_order,
    )


def parse_contents(contents_path: Path) -> tuple[dict[str, Any], list[str]]:
    modules: list[dict[str, Any]] = []
    chapters: list[dict[str, Any]] = []
    local_errors: list[str] = []
    saw_modules = False
    current_module: dict[str, Any] | None = None
    current_chapter: dict[str, Any] | None = None

    for raw_line in contents_path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("# ") or line.startswith("## ") and line == "##":
            continue

        module_match = MODULE_HEADING_RE.match(line)
        if module_match:
            saw_modules = True
            current_module = {
                "id": module_match.group(1),
                "title": module_match.group(2),
                "chapters": [],
            }
            modules.append(current_module)
            current_chapter = None
            continue

        chapter_match = CHAPTER_HEADING_RE.match(line)
        if chapter_match:
            current_chapter = {
                "dir": chapter_match.group(1),
                "title": chapter_match.group(2),
                "lessons": [],
            }
            if saw_modules:
                if current_module is None:
                    local_errors.append(
                        f"{contents_path}: chapter heading appears before a module heading: {line!r}"
                    )
                else:
                    current_module["chapters"].append(current_chapter)
            else:
                chapters.append(current_chapter)
            continue

        lesson_match = LESSON_LINE_RE.match(line)
        if lesson_match:
            if current_chapter is None:
                local_errors.append(
                    f"{contents_path}: lesson line appears before first chapter heading: {line!r}"
                )
            else:
                current_chapter["lessons"].append(lesson_match.group(1))

    if saw_modules and not modules:
        local_errors.append(f"{contents_path}: no module headings found")
    if not saw_modules and not chapters:
        local_errors.append(f"{contents_path}: no chapter headings found")

    return {"uses_modules": saw_modules, "modules": modules, "chapters": chapters}, local_errors


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


def compare_chapter_lists(
    spine_chapters: list[dict[str, Any]],
    contents_chapters: list[dict[str, Any]],
    label: str,
    results: ValidationResults,
) -> None:
    if len(spine_chapters) != len(contents_chapters):
        results.add_error(
            f"{label}: chapter count mismatch between spine ({len(spine_chapters)}) "
            f"and CONTENTS.md ({len(contents_chapters)})"
        )

    for index in range(min(len(spine_chapters), len(contents_chapters))):
        s_ch = spine_chapters[index]
        c_ch = contents_chapters[index]
        s_dir = s_ch.get("dir")
        s_title = s_ch.get("title")
        c_dir = c_ch.get("dir")
        c_title = c_ch.get("title")

        if s_dir != c_dir or s_title != c_title:
            results.add_error(
                f"{label}: chapter #{index + 1} mismatch; "
                f"spine=({s_dir!r}, {s_title!r}) vs CONTENTS=({c_dir!r}, {c_title!r})"
            )

        s_lessons = s_ch.get("lessons", [])
        if not isinstance(s_lessons, list):
            continue
        s_titles = [lesson.get("title") for lesson in s_lessons if isinstance(lesson, dict)]
        c_titles = c_ch.get("lessons", [])
        if s_titles != c_titles:
            results.add_error(
                f"{label}: lesson title/order mismatch in {s_dir or c_dir}; "
                f"spine={s_titles!r} vs CONTENTS={c_titles!r}"
            )


def check_spine_contents_parity(
    spine_data: dict[str, Any],
    contents_data: dict[str, Any],
    course_root: Path,
    results: ValidationResults,
) -> None:
    uses_modules, spine_modules = get_spine_modules(spine_data)
    contents_uses_modules = bool(contents_data.get("uses_modules"))

    if uses_modules != contents_uses_modules:
        results.add_error(
            f"{course_root}: spine/CONTENTS structure mismatch; "
            f"spine uses_modules={uses_modules} vs CONTENTS uses_modules={contents_uses_modules}"
        )
        return

    if uses_modules:
        contents_modules = contents_data.get("modules", [])
        if len(spine_modules) != len(contents_modules):
            results.add_error(
                f"{course_root}: module count mismatch between spine ({len(spine_modules)}) "
                f"and CONTENTS.md ({len(contents_modules)})"
            )

        for index in range(min(len(spine_modules), len(contents_modules))):
            s_mod = spine_modules[index]
            c_mod = contents_modules[index]
            s_id = s_mod.get("id")
            s_title = s_mod.get("title")
            c_id = c_mod.get("id")
            c_title = c_mod.get("title")
            if s_id != c_id or s_title != c_title:
                results.add_error(
                    f"{course_root}: module #{index + 1} mismatch; "
                    f"spine=({s_id!r}, {s_title!r}) vs CONTENTS=({c_id!r}, {c_title!r})"
                )
            s_chapters = s_mod.get("chapters", [])
            c_chapters = c_mod.get("chapters", [])
            if isinstance(s_chapters, list) and isinstance(c_chapters, list):
                compare_chapter_lists(
                    spine_chapters=s_chapters,
                    contents_chapters=c_chapters,
                    label=f"{course_root} {s_id or c_id}",
                    results=results,
                )
        return

    compare_chapter_lists(
        spine_chapters=spine_modules[0].get("chapters", []) if spine_modules else [],
        contents_chapters=contents_data.get("chapters", []),
        label=str(course_root),
        results=results,
    )


def validate_structure_metadata(
    spine_data: dict[str, Any], course_root: Path, results: ValidationResults
) -> None:
    uses_modules, modules = get_spine_modules(spine_data)
    refs = collect_course_refs(spine_data)

    seen_modules: dict[str, str] = {}
    if uses_modules:
        for module in modules:
            if not isinstance(module, dict):
                continue
            module_id = module.get("id")
            if not isinstance(module_id, str):
                continue
            previous_module = seen_modules.get(module_id)
            if previous_module is not None:
                results.add_error(
                    f"{course_root}: duplicate module id {module_id!r} in {previous_module} and {module_id}"
                )
            else:
                seen_modules[module_id] = module_id

    seen_chapters: dict[str, str] = {}
    for _, chapter in iter_spine_chapters(spine_data):
        chapter_dir = chapter.get("dir")
        if not isinstance(chapter_dir, str):
            continue
        previous_chapter = seen_chapters.get(chapter_dir)
        if previous_chapter is not None:
            results.add_error(
                f"{course_root}: duplicate chapter dir {chapter_dir!r} found in multiple locations"
            )
        else:
            seen_chapters[chapter_dir] = chapter_dir

        seen_lesson_ids: set[str] = set()
        lessons = chapter.get("lessons", [])
        if not isinstance(lessons, list):
            continue
        for lesson in lessons:
            if not isinstance(lesson, dict):
                continue
            lesson_id = lesson.get("id")
            if not isinstance(lesson_id, str):
                continue
            if lesson_id in seen_lesson_ids:
                results.add_error(
                    f"{course_root}: duplicate lesson id {lesson_id!r} inside {chapter_dir}"
                )
            seen_lesson_ids.add(lesson_id)

    if not uses_modules and len(refs.chapter_dirs) >= 10:
        results.add_warning(
            f"{course_root}: chapter-only course has {len(refs.chapter_dirs)} chapters; "
            "consider grouping the spine into modules."
        )


def validate_dependencies(
    spine_data: dict[str, Any], course_root: Path, results: ValidationResults
) -> None:
    refs = collect_course_refs(spine_data)

    for _, chapter_dir, lesson in iter_spine_lessons(spine_data):
        lesson_id = lesson.get("id")
        depends_on = lesson.get("depends_on", [])
        if not isinstance(lesson_id, str) or not isinstance(depends_on, list):
            continue

        lesson_ref = f"{chapter_dir}/{lesson_id}"
        current_index = refs.lesson_order.get(lesson_ref)
        for dependency in depends_on:
            if dependency not in refs.lesson_refs:
                results.add_error(
                    f"{course_root}: {lesson_ref} depends_on unknown lesson {dependency!r}"
                )
                continue
            if dependency == lesson_ref:
                results.add_error(f"{course_root}: {lesson_ref} cannot depend on itself")
                continue
            dependency_index = refs.lesson_order.get(dependency)
            if (
                current_index is not None
                and dependency_index is not None
                and dependency_index >= current_index
            ):
                results.add_error(
                    f"{course_root}: {lesson_ref} depends_on {dependency!r}, "
                    "but dependencies must point to earlier lessons"
                )


def validate_progress_targets(
    progress_data: dict[str, Any], spine_data: dict[str, Any], course_root: Path, results: ValidationResults
) -> None:
    refs = collect_course_refs(spine_data)

    last_completed = progress_data.get("last_completed")
    if isinstance(last_completed, str) and last_completed not in refs.lesson_refs:
        results.add_error(f"{course_root}: last_completed points to unknown lesson {last_completed!r}")

    next_target = progress_data.get("next_target")
    if isinstance(next_target, str) and next_target not in refs.lesson_refs:
        results.add_error(f"{course_root}: next_target points to unknown lesson {next_target!r}")

    current_target = progress_data.get("current_target")
    if not isinstance(current_target, dict):
        return

    target_type = current_target.get("type")
    target_ref = current_target.get("ref")
    if not isinstance(target_type, str) or not isinstance(target_ref, str):
        return

    if target_type == "lesson" and target_ref not in refs.lesson_refs:
        results.add_error(f"{course_root}: current_target lesson ref is unknown: {target_ref!r}")
    elif target_type == "chapter" and target_ref not in refs.chapter_dirs:
        results.add_error(f"{course_root}: current_target chapter ref is unknown: {target_ref!r}")
    elif target_type == "module" and target_ref not in refs.module_ids:
        results.add_error(f"{course_root}: current_target module ref is unknown: {target_ref!r}")
    elif target_type == "assessment":
        if target_ref.startswith("module:") and target_ref.split(":", 1)[1] not in refs.module_ids:
            results.add_error(
                f"{course_root}: current_target assessment module ref is unknown: {target_ref!r}"
            )
        elif target_ref.startswith("chapter:") and target_ref.split(":", 1)[1] not in refs.chapter_dirs:
            results.add_error(
                f"{course_root}: current_target assessment chapter ref is unknown: {target_ref!r}"
            )
        elif target_ref.startswith("lesson:") and target_ref.split(":", 1)[1] not in refs.lesson_refs:
            results.add_error(
                f"{course_root}: current_target assessment lesson ref is unknown: {target_ref!r}"
            )
    elif target_type == "replan":
        if target_ref.startswith("module:") and target_ref.split(":", 1)[1] not in refs.module_ids:
            results.add_error(f"{course_root}: current_target replan module ref is unknown: {target_ref!r}")
        elif target_ref.startswith("chapter:") and target_ref.split(":", 1)[1] not in refs.chapter_dirs:
            results.add_error(
                f"{course_root}: current_target replan chapter ref is unknown: {target_ref!r}"
            )


def test_glob_statically_scoped(chapter_dir: str, lesson_id: str, test_glob: str) -> bool:
    normalized = test_glob.replace("\\", "/")
    required_prefix = f"{chapter_dir}/{lesson_id}"
    return required_prefix in normalized and not normalized.startswith("/")


def validate_test_glob_scope(
    chapter_dir: str, lesson_id: str, test_glob: str, course_root: Path, results: ValidationResults
) -> None:
    prefix = f"{chapter_dir}/{lesson_id}"
    if ".." in Path(test_glob).parts or Path(test_glob).is_absolute():
        results.add_error(
            f"{course_root}: test_glob for {chapter_dir}/{lesson_id} cannot use absolute or parent traversal paths: {test_glob!r}"
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


def expected_selector(chapter_dir: str, lesson_id: str) -> str:
    chapter_num = chapter_dir.removeprefix("Ch")
    lesson_num = lesson_id.removeprefix("L")
    return f"lesson_ch{chapter_num}_l{lesson_num}"


def validate_main_test_selector(
    chapter_dir: str,
    lesson_id: str,
    test_glob: str,
    lesson_selector: Any,
    seen_selectors: dict[str, str],
    course_root: Path,
    results: ValidationResults,
) -> None:
    lesson_ref = f"{chapter_dir}/{lesson_id}"
    if ".." in Path(test_glob).parts or Path(test_glob).is_absolute():
        results.add_error(
            f"{course_root}: {lesson_ref} main_test-style test_glob must stay inside the course root: {test_glob!r}"
        )
        return

    if not isinstance(lesson_selector, str) or not lesson_selector.strip():
        results.add_error(
            f"{course_root}: {lesson_ref} uses main_test-style test_glob {test_glob!r} but has no lesson_selector"
        )
        return

    match = LESSON_SELECTOR_RE.match(lesson_selector)
    if not match:
        results.add_error(
            f"{course_root}: {lesson_ref} lesson_selector must match "
            f"'lesson_ch<chapter>_l<lesson>'; got {lesson_selector!r}"
        )
    else:
        expected = expected_selector(chapter_dir, lesson_id)
        if lesson_selector != expected:
            results.add_error(
                f"{course_root}: {lesson_ref} lesson_selector should be {expected!r}; got {lesson_selector!r}"
            )

    previous = seen_selectors.get(lesson_selector)
    if previous is not None and previous != lesson_ref:
        results.add_error(
            f"{course_root}: duplicate lesson_selector {lesson_selector!r} for {lesson_ref} and {previous}"
        )
    else:
        seen_selectors[lesson_selector] = lesson_ref

    if not (course_root / test_glob).exists():
        results.add_warning(
            f"{course_root}: spine uses {test_glob!r} for {lesson_ref}, but the file does not exist yet."
        )


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
    if not isinstance(spine_data, dict):
        results.add_error(f"{spine_path}: root document must be an object")
        return

    progress_path = None
    progress_data: dict[str, Any] | None = None
    for candidate in ("progress.yaml", "progress.yml", "progress.json"):
        path = course_dir / candidate
        if path.exists():
            progress_path = path
            break

    if progress_path is None:
        results.add_warning(f"{course_root}: missing optional course/progress.yaml|yml|json")
    else:
        try:
            loaded_progress = load_structured_file(progress_path)
            validate_schema(loaded_progress, progress_schema, str(progress_path), results)
            if isinstance(loaded_progress, dict):
                progress_data = loaded_progress
        except Exception as exc:  # pragma: no cover - parse failure branch
            results.add_error(f"{progress_path}: failed to parse ({exc})")

    validate_structure_metadata(spine_data, course_root, results)
    validate_dependencies(spine_data, course_root, results)
    if progress_data is not None:
        validate_progress_targets(progress_data, spine_data, course_root, results)

    if contents_path.exists():
        parsed_contents, contents_errors = parse_contents(contents_path)
        for err in contents_errors:
            results.add_error(err)
        check_spine_contents_parity(spine_data, parsed_contents, course_root, results)
    else:
        results.add_warning(
            f"{course_root}: missing CONTENTS.md; skipping spine/CONTENTS parity for this root"
        )

    seen_selectors: dict[str, str] = {}
    for _, chapter_dir, lesson in iter_spine_lessons(spine_data):
        lesson_id = lesson.get("id")
        test_glob = lesson.get("test_glob")
        if not isinstance(lesson_id, str) or not isinstance(test_glob, str):
            continue

        if MAIN_TEST_GLOB_RE.match(test_glob):
            validate_main_test_selector(
                chapter_dir=chapter_dir,
                lesson_id=lesson_id,
                test_glob=test_glob,
                lesson_selector=lesson.get("lesson_selector"),
                seen_selectors=seen_selectors,
                course_root=course_root,
                results=results,
            )
        else:
            results.add_warning(
                f"{course_root}: {chapter_dir}/{lesson_id} uses legacy per-lesson test_glob "
                f"{test_glob!r}; migrate to main_test-style files + lesson_selector when feasible."
            )
            validate_test_glob_scope(
                chapter_dir=chapter_dir,
                lesson_id=lesson_id,
                test_glob=test_glob,
                course_root=course_root,
                results=results,
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
