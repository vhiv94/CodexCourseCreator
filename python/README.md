# Python courses (`python/`)

Every **Python** course in this repository gets its **own subdirectory** under **`python/`** (for example `python/fundamentals/`, `python/your-topic/`).

## Layout and tooling

| Convention | Detail |
|------------|--------|
| **One folder per course** | `python/<course-slug>/` — short, lowercase, hyphenated (filesystem-safe). |
| **uv only** | Manage the project with **[uv](https://docs.astral.sh/uv/)**: `uv init`, `uv sync`, `uv add`, `uv run pytest`, … — not ad-hoc `pip install` + hand-written `requirements.txt` unless a course explicitly documents an exception in its `overview.md`. |
| **Course artifacts** | Same shape as the reference course: `course/spine.yaml`, `course/overview.md`, optional `course/glossary.md`, `course/progress.yaml`, root **`CONTENTS.md`** next to `course/`, chapter dirs **`Chk/`** with `Ln.md` (+ optional hints), module-root `main.py`, append-only module-root `main_test.py` with selector-scoped lesson tests. |
| **Schema** | `spine.yaml` validates against the **repository root** [`course/spine.schema.json`](../course/spine.schema.json) (use `@course/spine.schema.json` in prompts from repo root). |

## New course: Atlas + uv

When **Atlas** plans a **new** Python course:

1. **Create** `python/<course-slug>/` if it does not exist.
2. If there is **no** `pyproject.toml` in that directory, **run `uv init`** there. Prefer **`uv init --no-readme`** so uv does not create a default `README.md` that collides with the course `README.md` you will add—or use **`uv init --bare`** if you want only a minimal `pyproject.toml` and will flesh out the tree afterward.
3. **Add** test dependencies the overview commits to — at minimum **`uv add pytest`** for the usual Riley/pytest layout, then **`uv sync`**.
4. Write **spine**, **CONTENTS.md**, **overview**, optional glossary, and initialize **`course/progress.yaml`** as usual.

Reference implementations:

- **`python/fundamentals/`** for a larger real course.
- **`python/reference-module/`** for a compact worked example of `main.py` + append-only `main_test.py` + selector-scoped lesson flow.

## Bootstrap command sequence (human/agent preflight)

From repository root:

```bash
mkdir -p python/<course-slug>
cd python/<course-slug>
uv init --no-readme
uv add pytest
uv sync
mkdir -p course
printf "last_completed: null\n" > course/progress.yaml
cd ../../
python3 scripts/validate_repo.py
```

If `spine.yaml`/`CONTENTS.md` are not generated yet, run Atlas first, then rerun validation.

## Canonical lesson selector contract

For module-root `main_test.py` flow, each lesson in `course/spine.*` defines:

- `test_glob: main_test.py`
- `lesson_selector: lesson_ch<chapter>_l<lesson>` (example: `lesson_ch2_l3`)

Run one lesson with:

```bash
uv run pytest main_test.py -m lesson_ch2_l3
```

Riley appends new lesson blocks to `main_test.py` (never rewrites unrelated prior lesson blocks).

## `main_test.py` growth guardrails

For Python courses, apply these thresholds to decide when to stop single-file growth:

- Plan a split when `main_test.py` exceeds **900 lines** or about **120 tests**.
- Require a split before `main_test.py` exceeds **1400 lines** or about **180 tests**.
- Keep selector-scoped runs (`uv run pytest <test_glob> -m <lesson_selector>`) around **<= 2 seconds** in normal local development.
- Keep per-course full test execution around **<= 45 seconds**.

When splitting, move to chapter-level test files (`main_test_ch1.py`, `main_test_ch2.py`, ...):

1. Update each lesson's spine row to the chapter file via `test_glob` (for example `main_test_ch3.py`).
2. Keep `lesson_selector` unchanged (`lesson_ch<chapter>_l<lesson>`).
3. Preserve append-only semantics per file scope: each chapter file grows forward only, and unrelated prior lesson blocks stay untouched.

## Migration strategy for existing legacy courses

If a course still uses per-lesson test files (`Ch#/L#.py`), migrate incrementally:

1. Keep existing `Ch#/L#.py` files in place.
2. Create/extend module-root `main_test.py` with lesson blocks marked by unique selectors (`lesson_ch<chapter>_l<lesson>`).
3. Update `course/spine.*` lesson rows in small batches from legacy `test_glob` to:
   - `test_glob: main_test.py`
   - `lesson_selector: lesson_ch<chapter>_l<lesson>`
4. Run `python3 scripts/validate_repo.py` and verify each migrated lesson with:
   - `uv run pytest main_test.py -m <lesson_selector>`
5. Delete legacy `Ch#/L#.py` only after every lesson has cut over and remains green.

### Rollback (safe fallback)

- Revert only the current batch's spine rows back to original legacy `test_glob` values.
- Keep `main_test.py` additions (they can stay while rollback is in effect).
- Run the old lesson-local command against `Ch#/L#.py` until the batch is fixed.
- Resume migration with smaller batches if needed.

## Governance and batching in day-to-day flow

- Stay in **Riley/Marsh flow** for normal next-lesson work on an unchanged spine.
- Re-engage **Atlas** before lesson generation when chapter sequencing, lesson scope, or audience constraints need replanning.
- Keep Maestro batches to **1-3 lesson targets** per request; validate between batches to catch drift early.
