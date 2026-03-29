# Course creator (multi-agent TDD courses)

This workspace holds **conventions and Cursor rules** for building **capstone-style, lesson-by-lesson courses**: each lesson has **markdown + selector-scoped tests in `main_test.py`**, learners implement in **`main.py`** and supporting modules (or your documented layout), and verification is **automated tests** only.

**Agent roles** (each is a Cursor rule under [`.cursor/rules/`](.cursor/rules/)):

| Role | Job |
|------|-----|
| **Maestro** | Orchestrator: reads `course/spine.*` and `course/progress.*`, emits **progress patches** and **copy-paste prompt packs** for the specialists. |
| **Atlas** | Learning architect: `course/spine.yaml` (or `.json`), root **`CONTENTS.md`**, **`course/overview.md`**, optional glossary. |
| **Riley** | Test author: append lesson-scoped test blocks to module-root **`main_test.py`** using per-lesson selectors. |
| **Dr. Marsh** | Lesson author: **`Chk/Ln.md`**, optional **`Chk/Ln.hints.md`** when the spine sets `hints: true`. |

**On-disk layout**: Linear **`Ch1/`**, **`Ch2/`**, … with **`L1.md`** and optional **`L1.hints.md`** per lesson, plus module-root **`main.py`** (learner entrypoint) and append-only **`main_test.py`** (all lesson tests). **`course/spine.*`** and **`CONTENTS.md`** must stay in sync (same chapter titles and lesson order).

Legacy per-lesson test files (`Ch#/L#.py`) are still migration-compatible, but new/updated course planning should use `main_test.py` + `lesson_selector`.

**Progress**: Track advancement in **`course/progress.yaml`** (see `course/progress.schema.json`). Typical start: `last_completed: null`.

**Cursor note**: Cursor does not call agents automatically. You use **Maestro in chat**; it tells you **which rule to attach** and **what to paste** into Composer (or a new chat) for Atlas, Riley, or Marsh.

---

## Suggested workflow in Cursor (Maestro-driven)

1. **New course**  
   Open **one chat with Maestro** → paste your **topic** and **level** → Maestro gives an **Atlas prompt pack** → run it in **Composer** with the **Atlas** rule attached → you end up with **`course/spine.*`**, **`CONTENTS.md`**, **`course/overview.md`** (and optional empty **`Chk/`** directories). Initialize **`course/progress.yaml`** with **`last_completed: null`**.

2. **Each next lesson** (after you have finished the previous one — tests green, ready for the next lesson’s materials)  
   Tell Maestro e.g. **`Done with Ch1/L1`**. Maestro updates **progress** instructions and emits:
  - **Riley prompt** → run in **Composer** with the **Riley** rule (appends selector-scoped tests in **`main_test.py`**),
   - then **Marsh prompt** → **Marsh** rule (creates **`Chk/Ln.md`** and optional hints).

3. **You** implement against the new tests (**TDD**) in **`src/`** (or your repo’s layout).

4. **Replan or extend the course**  
   Tell **Maestro** → it emits a fresh **Atlas** prompt (narrow delta or full spine revision) before **Riley/Marsh** resume.

**Convention**: Keep **one long-lived Maestro thread** per course if you want continuity; use **fresh Composer runs** for **Riley** and **Marsh** so context stays clean. Maestro’s pack may say explicitly: *open a new chat, attach rule X, paste the block below.*

---

## Bootstrap + preflight (new course)

Before generating lessons, create and validate the course shell first.

1. Create course folder (example): `mkdir -p python/<course-slug> && cd python/<course-slug>`
2. Initialize tooling: `uv init --no-readme`
3. Add baseline test dependency: `uv add pytest`
4. Sync environment: `uv sync`
5. Initialize progress file: create `course/progress.yaml` with:

```yaml
last_completed: null
```

6. From repository root, run validation:

```bash
python3 scripts/validate_repo.py
```

Use this preflight every time Atlas updates `course/spine.*`/`CONTENTS.md`, and before asking Riley/Marsh to generate lesson assets.

---

## Governance: replan vs continue

- Continue with **Riley + Marsh** when the existing spine still fits and you are advancing to the immediate next lesson.
- Replan with **Atlas** when scope, chapter order, prerequisites, project direction, or audience level changes.
- If `course/spine.*` changes, run `python3 scripts/validate_repo.py` before resuming Riley/Marsh so contracts stay aligned.

---

## Maestro batching guidance

To avoid context-window overload and accidental drift, batch lesson generation in small chunks.

- Recommended batch size: **1-3 lessons** at a time.
- Prefer chapter-local batches (for example `Ch2/L1` -> `Ch2/L3`) before crossing into a new chapter.
- After each batch, validate and run lesson-local tests before requesting the next batch.
- In Maestro prompts, include explicit lesson selectors (for example `Ch3/L2`) and avoid open-ended "continue everything" requests.
- Canonical test selector contract is pytest marker-based: `lesson_ch<chapter>_l<lesson>` (for example `lesson_ch3_l2`), run as `uv run pytest main_test.py -m lesson_ch3_l2`.

---

## `main_test.py` growth guardrails

Use these guardrails to keep lesson-scoped test execution fast as a course grows.

- **Soft size threshold:** when `main_test.py` passes **900 lines** or about **120 test functions**, plan a split in the next batch.
- **Hard size threshold:** do not keep adding to a single `main_test.py` past **1400 lines** or about **180 test functions**.
- **Scoped perf threshold:** a selector-scoped run (`uv run pytest <test_glob> -m <lesson_selector>`) should usually finish in **<= 2 seconds** on local dev hardware.
- **Full-suite perf threshold:** running the current test files for one course should usually finish in **<= 45 seconds**.

### Split strategy (chapter-level files)

When a threshold is exceeded, switch from one-file growth to chapter-level files while preserving selector scoping and append-only semantics:

1. Create chapter files such as `main_test_ch1.py`, `main_test_ch2.py`, etc.
2. Keep spine rows lesson-local by setting `test_glob` to the chapter file that owns that lesson (for example `main_test_ch2.py`) and keeping the same marker contract (`lesson_ch2_l3`).
3. Treat each chapter file as append-only history for that chapter: add new lessons to the end of that file and never rewrite unrelated prior lesson blocks.
4. Do not mix new lessons for a chapter back into the old monolithic file after that chapter has been split.

This split keeps lesson execution targeted, allows chapter-sized maintenance, and preserves migration safety.

---

## Migration path: `Ch#/L#.py` -> append-only `main_test.py`

Use this when modernizing existing courses that still point lessons to per-lesson test files.

1. **Inventory current lessons**  
   For each lesson in `course/spine.*`, record legacy `test_glob` (for example `Ch2/L3.py`) and the target selector you will assign (`lesson_ch2_l3`).

2. **Create/prepare `main_test.py` without deleting legacy tests**  
   Keep legacy `Ch#/L#.py` files in place during migration. Add lesson blocks to `main_test.py` with unique pytest markers matching spine `lesson_selector`.

3. **Move spine entries in small batches**  
   Update a small set of lessons (recommended 1-3) from legacy `test_glob` to:
   - `test_glob: main_test.py`
   - `lesson_selector: lesson_ch<chapter>_l<lesson>`

4. **Validate after each batch**  
   Run `python3 scripts/validate_repo.py`, then run scoped tests for each migrated lesson:
   - `uv run pytest main_test.py -m <lesson_selector>`

5. **Cut over fully, then clean up**  
   Once all lessons are migrated and green, treat `main_test.py` as canonical append-only history. Remove legacy `Ch#/L#.py` files only after the full cutover is stable.

### Rollback guidance

- **Batch rollback:** if a migrated batch is unstable, revert only that batch's spine rows to original `test_glob` values and run the prior lesson-local command(s) against `Ch#/L#.py`.
- **File safety:** do not delete legacy `Ch#/L#.py` files until full cutover is verified; this keeps rollback one edit away.
- **Selector safety:** if a selector collides or is misnamed, fix `lesson_selector` in spine and marker names in `main_test.py`, then re-run validation.
- **Operational default:** when in doubt, pause migration, keep legacy execution for active lessons, and resume in smaller batches.

---

## Related files

- **`course/spine.schema.json`** — spine structure (chapters, lessons, `test_glob`, `lesson_selector`, `depends_on`, `hints`).
- **`course/progress.schema.json`** — progress tracking for Maestro.
- **`scripts/validate_repo.py`** — repo-level validation (schema checks, spine/`CONTENTS.md` parity, and test scope via `test_glob` + `lesson_selector`).
- **`scripts/check_test_regression.py`** — git-history guardrail for CI (blocks deleted prior lesson tests and removed/changed historical lesson selectors).
- **`.github/workflows/ci.yml`** — pull-request CI enforcing repository contracts and regression checks.
- **`course/guides/test-authoring/`** — optional stack notes (Vitest, pytest, Jest, …) for Riley-style test setup.
- **`python/`** — **one subdirectory per Python course** (e.g. `python/fundamentals/`). New courses use **[uv](https://docs.astral.sh/uv/)**; **Atlas** may **`uv init`** in `python/<slug>/` when `pyproject.toml` is absent — see [`python/README.md`](python/README.md). A compact worked reference for this flow lives at [`python/reference-module/`](python/reference-module/).

A fuller product spec, handoff diagram, and optional roles (Sage, Quinn, Vera) are in **`multi-agent_course_creator_32d63945.plan.md`** — usually under **`~/.cursor/plans/`** on your machine; copy it into this repo if you want it versioned with the course.
