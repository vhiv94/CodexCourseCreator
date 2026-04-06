# Course Creator

This repository defines the current system for generating adaptive, project-based courses with structured planning, lesson-first authoring rules, and repository validation.

## Start here

- Read `AGENTS.md` for role boundaries and the current authoring flow.
- Read `SCOPE.md` for course-design rules: scoping, assessments, modules, chapters, lessons, and adaptive generation.
- Read `FINAL_PRODUCT.md` for the long-term website vision.

## Core contracts

- `course/spine.schema.json` defines the planning structure.
- `course/progress.schema.json` defines learner and orchestration state.
- `scripts/validate_repo.py` validates schema compliance, `CONTENTS.md` parity, and course-contract rules.
- `scripts/check_test_regression.py` guards against accidental historical test regressions for courses that keep append-only test history.

## Repository shape

- `python/` contains example and real Python course roots.
- `.cursor/rules/` contains the role rules used in Cursor.
- `course/` contains shared schemas, examples, templates, and guides.
- `course/reference-module/` is the canonical minimal worked example for the current workflow.
- `CHATLOG.md` keeps the project chat history.

## Quickstart

1. Inspect `course/reference-module/` for the canonical minimal lesson-first example.
2. Create or open a real course root such as `python/<course-slug>/` when you are starting a new Python course project.
3. Initialize that Python project with `uv init --no-readme`, `uv add pytest`, and `uv sync` only when the course needs its own environment and test tooling.
4. Start `course/progress.*` with a short-answer pre-structure assessment before deciding the course shape.
5. Create or update `course/spine.*` and `CONTENTS.md`, keeping `delivery.assessment_format: short_answer`, `prestructure_assessment: true`, and `prechapter_assessments: true` unless the course has a documented exception.
6. Before generating a chapter for the first time, run a short-answer prechapter assessment for that chapter.
7. Author the next narrow lesson and assignment first, usually one lesson at a time unless the chapter is already well scoped for a small batch.
8. Add tests afterward only when the selected lesson metadata says they should exist.
9. Run `python3 scripts/validate_repo.py` from the repository root.

Use the new root docs above as the primary source of truth instead of relying on `README.md` for all process detail.
