# Course Creator

This repository defines the current system for generating adaptive, project-based courses with structured planning, role rules, and repository validation.

## Start here

- Read `AGENTS.md` for role boundaries and the current authoring flow.
- Read `SCOPE.md` for course-design rules: scoping, assessments, modules, chapters, lessons, and adaptive generation.
- Read `FINAL_PRODUCT.md` for the long-term website vision.

## Core contracts

- `course/spine.schema.json` defines the planning structure.
- `course/progress.schema.json` defines learner and orchestration state.
- `scripts/validate_repo.py` validates schema compliance, `CONTENTS.md` parity, and course-contract rules.
- `scripts/check_test_regression.py` guards against accidental historical test regressions.

## Repository shape

- `python/` contains example and real Python course roots.
- `.cursor/rules/` contains the role rules used in Cursor.
- `course/` contains shared schemas, examples, templates, and guides.
- `CHATLOG.md` keeps the project chat history.

## Quickstart

1. Create or open a course root such as `python/<course-slug>/`.
2. Initialize the project if needed with `uv init --no-readme`, `uv add pytest`, and `uv sync`.
3. Create or update `course/spine.*`, `course/progress.*`, and `CONTENTS.md`.
4. Run `python3 scripts/validate_repo.py` from the repository root.

Use the new root docs above as the primary source of truth instead of relying on `README.md` for all process detail.
