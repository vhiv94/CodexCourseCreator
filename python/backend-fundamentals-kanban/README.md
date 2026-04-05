# Backend Fundamentals - Kanban Lite

This course teaches backend fundamentals through one coherent project: a self-hosted **Kanban Lite API** built with FastAPI and SQLite.

It now serves as the pilot course for the redesigned flow:

- intake assessment informs scope and pacing;
- the full plan uses `modules -> chapters -> lessons`;
- content is still generated in chapter-sized batches rather than assuming the whole course is authored at once.

Right now, the planned course structure lives in `course/spine.yaml` and `CONTENTS.md`, while the next authored sequence is the pre-Ch1 readiness checkpoint plus the Chapter 1 lesson batch under `course/M1/Ch1/`.

## Quick start

From this directory:

```bash
uv sync
uv run pytest main_test.py -m lesson_ch1_l1
```

## Dependency management

Use `uv` commands for this course:

```bash
uv add <package-name>
uv remove <package-name>
```

Do not use ad hoc `pip install` for this course workflow.

## Course artifacts

- `course/spine.yaml`
- `course/overview.md`
- `course/glossary.md`
- `course/progress.yaml`
- `course/M#/Ch#/L#.md` for this module-aware course's lesson prose, plus sibling `-hint.md` files when hints are enabled
- `CONTENTS.md`
- `src/` for learner/source modules when needed
- `main.py`
- `main_test.py`
