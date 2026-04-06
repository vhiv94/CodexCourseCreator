# Python courses (`python/`)

Every **Python** course in this repository gets its **own subdirectory** under **`python/`** (for example `python/fundamentals/`, `python/your-topic/`).

## Layout and tooling

| Convention | Detail |
|------------|--------|
| **One folder per course** | `python/<course-slug>/` — short, lowercase, hyphenated (filesystem-safe). |
| **uv only** | Manage the project with **[uv](https://docs.astral.sh/uv/)**: `uv init`, `uv sync`, `uv add`, `uv run pytest`, … — not ad-hoc `pip install` + hand-written `requirements.txt` unless a course explicitly documents an exception in its `overview.md`. |
| **Course artifacts** | Same planning shape as the canonical example in `course/reference-module/`: `course/spine.yaml`, `course/overview.md`, optional `course/glossary.md`, `course/progress.yaml`, root **`CONTENTS.md`** next to `course/`, lesson prose under `course/Ch#/L#.md` for chapter-only courses or `course/M#/Ch#/L#.md` for module-aware courses (with optional sibling `-hint.md` files), learner/source code under `src/` when needed, module-root `main.py`, and optional module-root `main_test.py` with selector-scoped lesson tests when the course uses them. |
| **Schema** | `spine.yaml` validates against the **repository root** [`course/spine.schema.json`](../course/spine.schema.json) (use `@course/spine.schema.json` in prompts from repo root). |

## New course: planning + uv

When the planning pass defines a **new** Python course:

1. **Create** `python/<course-slug>/` if it does not exist.
2. If there is **no** `pyproject.toml` in that directory, **run `uv init`** there. Prefer **`uv init --no-readme`** so uv does not create a default `README.md` that collides with the course `README.md` you will add—or use **`uv init --bare`** if you want only a minimal `pyproject.toml` and will flesh out the tree afterward.
3. **Add** test dependencies only if the course overview commits to tests — usually **`uv add pytest`** for a pytest-based flow, then **`uv sync`**.
4. Write **spine**, **CONTENTS.md**, **overview**, optional glossary, and initialize **`course/progress.yaml`** as usual.

For new Python courses, prefer this root split:

- `course/` for planning files and lesson markdown
- `src/` for learner/source modules and packages
- root `main.py` and optional `main_test.py` as stable entrypoints when the course uses them

Reference implementations:

- **`python/fundamentals/`** for a larger real course.
- **`course/reference-module/`** for the canonical minimal lesson-first workflow example using plain `python3`.
- **`python/reference-module/`** as a legacy archive of the earlier `uv` + selector-scoped pytest example.

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

If `spine.yaml`/`CONTENTS.md` are not generated yet, run planning first, then rerun validation.

## Optional lesson selector contract

For module-root `main_test.py` flow, a tested lesson in `course/spine.*` defines:

- `test_glob: main_test.py`
- `lesson_selector: lesson_ch<chapter>_l<lesson>` (example: `lesson_ch2_l3`)

Run one lesson with:

```bash
uv run pytest main_test.py -m lesson_ch2_l3
```

Test authoring appends new lesson blocks to `main_test.py` (never rewrites unrelated prior lesson blocks).

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

- Stay in the **lesson authoring first / optional test authoring second** flow for normal next-lesson work on an unchanged spine.
- Re-engage **planning** before lesson generation when chapter sequencing, lesson scope, or audience constraints need replanning.
- Prefer **1 lesson target** by default; expand to **2-3 lesson targets** only when the chapter is already well scoped. Validate between batches to catch drift early.
