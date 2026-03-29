# Chat log

## 2026-03-28 — README workflow + context

**User request:** Add the suggested Maestro-driven workflow from `multi-agent_course_creator_32d63945.plan.md` (lines 136–144 in the excerpt; full section “Suggested workflow in Cursor”) to `README.md`, plus any other relevant information.

**Assistant actions:**

- Replaced empty `README.md` with project overview: agent roles table, on-disk layout, progress file, Cursor handoff note, full **Suggested workflow in Cursor (Maestro-driven)** (new course → per-lesson Riley/Marsh → learner TDD → replan), thread/Composer convention, and pointers to schemas, test-authoring guides, and the full plan file.

---

## 2026-03-28 — `test-authoring-guide`

**User request:** Add per-ecosystem appendix patterns (Vitest, pytest, …) as non-agent docs (Quinn-rule deferred). Do not edit the attached plan file.

**Assistant actions:**

- Added `course/guides/test-authoring/README.md` — index of stack appendices and how they relate to Riley / `course/overview.md`.
- Added `course/guides/test-authoring/vitest.md` — layout, `test_glob`, config hints, scoped `vitest run`, fixtures, pitfalls, Riley checklist.
- Added `course/guides/test-authoring/pytest.md` — layout, discovery/config, scoped `pytest` invocation, `conftest` scope, pitfalls, Riley checklist.
- Added `course/guides/test-authoring/jest.md` — Jest-specific runner/config notes and checklist (optional vs Vitest).
- Updated `.cursor/rules/kwon-test-architect.mdc` — inputs reference `course/guides/test-authoring/` for ecosystem patterns.

**Note:** Plan file was not modified.

---

## 2026-03-28 — `maestro-progress`

**User request:** Specify `course/progress.yaml` (or JSON) schema, user utterances (e.g. `done Ch1/L1`), and Maestro output format (Riley block, Marsh block, optional Atlas replan). Do not edit the attached plan file.

**Assistant actions:**

- Added `course/progress.schema.json` (JSON Schema 2020-12): required `last_completed` (`Chk/Ln` or `null`), optional `next_target`, optional `notes`; `Chk/Ln` pattern aligned with spine lesson refs.
- Added `course/progress.example.yaml` and starter `course/progress.yaml` (`last_completed: null`).
- Expanded `.cursor/rules/maestro-orchestrator.mdc`: progress schema table, canonical utterance list, fixed output section order (progress patch → Riley → Marsh → optional Atlas), copy-paste templates for each block, completion / batching behavior, updated session checklist.
- Validated both progress YAML files with `jsonschema`.

**Note:** Plan file was not modified.

---

## 2026-03-28 — `lesson-template`

**User request:** Add lesson + optional hints templates (objectives, acceptance checklist in lesson; algorithm nudges only in hints for harder modules). Do not edit the attached plan file.

**Assistant actions:**

- Added `course/templates/lesson.md`: section skeleton with **learning objectives** (checkbox list), **acceptance criteria** checklist tied to public tests, assigned tasks without step-by-step solution, test path + lesson-local runner placeholder, misconceptions, further reading, and footer pointing algorithmic detail to `Ln.hints.md` when `hints: true`.
- Added `course/templates/lesson-hints.md`: optional sheet for spine `hints: true` only—when to open, orientation, **nudges**, optional **algorithm/pseudocode sketch**, pitfalls; explicitly forbids a full copy-paste solution.
- Updated `.cursor/rules/marsh-lesson-author.mdc`: inputs reference both templates; session checklist includes reading the appropriate template(s).

**Note:** Plan file was not modified.

---

## 2026-03-28 — `cursor-rules-pack`

**User request:** Author four `.cursor/rules/*.mdc` files — Atlas, Marsh, Riley (Kwon), Maestro — with forbidden-output lists and progress contract; do not edit the attached plan file.

**Assistant actions:**

- Added `.cursor/rules/maestro-orchestrator.mdc`: inputs (spine + progress), progress contract (`last_completed`, optional `next_target`/`notes`), outputs (progress patch + prompt packs), utterance patterns, forbidden outputs, session checklist.
- Added `.cursor/rules/atlas-learning-architect.mdc`: spine + `CONTENTS.md` + `course/overview.md` (+ optional glossary), schema alignment with `course/spine.schema.json`, forbidden outputs, checklist.
- Added `.cursor/rules/marsh-lesson-author.mdc`: `Chk/Ln.md` structure, optional `Ln.hints.md` when `hints: true`, pedagogy constraints, forbidden outputs, checklist.
- Added `.cursor/rules/kwon-test-architect.mdc`: per-lesson tests, `test_glob` scope, principles, forbidden outputs, checklist.

**Note:** Plan file was not modified.

---

## 2026-03-28 — `define-spine-schema`

**User request:** Finalize `course/spine.yaml` (or `.json`) schema: chapters, `Ch#/L#` paths, `test_glob`, `depends_on`, `hints`; document matching root `CONTENTS.md` format. Do not edit the attached plan file.

**Assistant actions:**

- Added `course/spine.schema.json` (JSON Schema draft 2020-12): `course_id`, `title`, `audience_level`, `chapters[]` with `dir` (`Ch#`), `title`, `lessons[]` with `id` (`L#`), `title`, `concept`, `project_step`, optional `reads` / `tasks_summary`, `test_glob`, `depends_on` (`Ch#/L#` refs), optional `hints`.
- Added `course/spine.example.yaml` and starter `course/spine.yaml`.
- Added `course/spine-and-contents.md` documenting filesystem layout, `CONTENTS.md` heading/numbering rules, and sync with spine titles/order.
- Validated both YAML files against the schema with Python `jsonschema`.

**Note:** Plan file was not modified.

---

## 2026-03-28 — Python fundamentals + Atlas prompt

**User request:** Per approved plan: test the Maestro system with a “learn the basics with Python” course for someone with no programming background—create `python/fundamentals` and an Atlas prompt; do not edit the plan file.

**Assistant actions:**

- Added [`python/fundamentals/ATLAS_PROMPT.md`](python/fundamentals/ATLAS_PROMPT.md): enable `atlas-learning-architect`, Maestro path caveat for nested `course/`, fenced paste block with output paths under `python/fundamentals/`, citations to `@course/spine.schema.json` and `@course/guides/test-authoring/pytest.md`, topic/audience/capstone constraints, Atlas forbidden outputs.

**Note:** Plan file was not modified.

---

## 2026-03-28 — Python fundamentals Atlas spine

**User request:** As Atlas, design a full beginner Python course under `python/fundamentals/`: `course/spine.yaml` (validate vs root `course/spine.schema.json`), `CONTENTS.md` mirroring spine verbatim, `course/overview.md` (pytest per `course/guides/test-authoring/pytest.md`), optional glossary; one capstone arc; no full lesson markdown, test code, or learner `src/` implementation.

**Assistant actions:**

- Added [`python/fundamentals/course/spine.yaml`](python/fundamentals/course/spine.yaml) — `course_id` `python-fundamentals-study-log`, six chapters (Ch1–Ch6), 21 lessons: CLI **study log** from `print` / strings through variables, input, control flow, functions, lists, files, dict settings, argv modes; `test_glob` `Chk/Ln.py` each; `hints: true` on Ch2/L4, Ch3/L4, Ch5/L3, Ch6/L1, Ch6/L3.
- Added [`python/fundamentals/CONTENTS.md`](python/fundamentals/CONTENTS.md) — headings `### Chk: ...` and numbered lesson titles match spine order/titles exactly.
- Added [`python/fundamentals/course/overview.md`](python/fundamentals/course/overview.md) — motivation, behavioral end-state, prerequisites, chapter map, pytest layout and `pytest Chk/Ln.py` from `python/fundamentals/`, shared fixtures expectation under `tests/support/`.
- Added [`python/fundamentals/course/glossary.md`](python/fundamentals/course/glossary.md) — beginner terms (interpreter, REPL, variable, function, etc.).
- Validated spine YAML with `jsonschema` against `course/spine.schema.json`.

---

## 2026-03-28 — Riley + Marsh prompts for Ch1/L1

**User request:** Maestro-style Riley and Marsh copy-paste prompts for only the first lesson of the Python fundamentals course.

**Assistant actions:**

- Emitted progress patch (`last_completed: null`, `next_target: Ch1/L1`), Riley block (`kwon-test-architect`) and Marsh block (`marsh-lesson-author`) for **Ch1/L1** using `python/fundamentals/course/spine.yaml` (`test_glob: Ch1/L1.py`, `depends_on: []`, `hints: false`); cites nested spine, overview, pytest guide, overview fixture note.

---

## 2026-03-28 — Riley Ch1/L1 pytest module

**User request:** Produce only the test file for Ch1/L1 matching `test_glob: Ch1/L1.py` under `python/fundamentals/`; deterministic; no learner `src/` solution; `depends_on: []`.

**Assistant actions:**

- Added [`python/fundamentals/Ch1/L1.py`](python/fundamentals/Ch1/L1.py) — subprocess runs `sys.executable` on learner entrypoint `src/main.py` (relative to course root); asserts exit 0, stdout is exactly one non-empty line (welcome); `main_script` fixture fails fast with path hint if entrypoint missing; footer comment with canonical `pytest Ch1/L1.py` from `python/fundamentals/`.
- Verified `pytest Ch1/L1.py` collection; without `src/main.py`, fixture assertion fails as expected (TDD).

---

## 2026-03-28 — Marsh Ch1/L1 lesson (no hints)

**User request:** Write `Ch1/L1.md` for **Hello from Python**; no `Ch1/L1.hints.md` (`hints: false`); align tasks and acceptance checklist with existing tests; absolute-beginner tone; no step-by-step solution.

**Assistant actions:**

- Added [`python/fundamentals/Ch1/L1.md`](python/fundamentals/Ch1/L1.md): concept (running Python, stdout, `print`, exit 0), project tie-in, objectives, tasks targeting `src/main.py` and contracts from [`python/fundamentals/Ch1/L1.py`](python/fundamentals/Ch1/L1.py), acceptance checklist (entrypoint path, exit 0, exactly one stdout line, non-empty visible text), `pytest Ch1/L1.py` from `python/fundamentals/`, misconceptions, optional reading; footer notes no hints file.

---

## 2026-03-28 — uv + `uv run pytest` for fundamentals

**User request:** User initialized uv; use `uv run pytest` for tests and remember that for future lesson-completion prompts.

**Assistant actions:**

- Ran `uv run pytest Ch1/L1.py` from `python/fundamentals/` — 2 passed.
- Updated [`python/fundamentals/course/overview.md`](python/fundamentals/course/overview.md): uv as dependency manager; canonical one-lesson command `uv run pytest Chk/Ln.py`, with note that plain `pytest` is OK only when venv is active.
- Updated [`python/fundamentals/Ch1/L1.py`](python/fundamentals/Ch1/L1.py) footer comment and [`python/fundamentals/Ch1/L1.md`](python/fundamentals/Ch1/L1.md) “how you’ll know you’re done” block to use `uv run pytest`.
- Wrote [`python/fundamentals/README.md`](python/fundamentals/README.md) with `uv run pytest Chk/Ln.py` pattern.
- Added [`python/fundamentals/course/progress.yaml`](python/fundamentals/course/progress.yaml): `last_completed: Ch1/L1`, `next_target: Ch1/L2`.
- Appended short **After `uv init`** section to [`python/fundamentals/ATLAS_PROMPT.md`](python/fundamentals/ATLAS_PROMPT.md) for agents.

---

## 2026-03-28 — Maestro handoff: next lesson Ch1/L2

**User request:** Next lesson (after Ch1/L1 complete per `python/fundamentals/course/progress.yaml`).

**Assistant actions:**

- Target **Ch1/L2** — *Build a Simple Banner*; `test_glob: Ch1/L2.py`, `depends_on: [Ch1/L1]`, `hints: false`.
- Emitted Maestro-style **progress** (unchanged YAML), **Riley** (`kwon-test-architect`) and **Marsh** (`marsh-lesson-author`) paste blocks with `@python/fundamentals/…` paths, `uv run pytest Ch1/L2.py` verification, no hints file. (Marsh block should cite lesson template at repo root [`course/templates/lesson.md`](course/templates/lesson.md), not under `python/fundamentals/`.)

---

## 2026-03-28 — Done Ch1/L2 → progress + Ch1/L3 handoff

**User request:** `done` (completed Ch1/L2; treat as Maestro **done Ch1/L2**).

**Assistant actions:**

- Ran `uv run pytest Ch1/L2.py` from `python/fundamentals/` — all passed.
- Updated [`python/fundamentals/course/progress.yaml`](python/fundamentals/course/progress.yaml) to `last_completed: Ch1/L2`, `next_target: Ch1/L3`.
- Emitted Maestro-style **Riley** / **Marsh** paste guidance for **Ch1/L3** — *Comment What Your Script Does* (`test_glob: Ch1/L3.py`, `depends_on: [Ch1/L2]`, `hints: false`).

---

## 2026-03-28 — Riley Ch1/L2 tests (`Ch1/L2.py`)

**User request:** Add only the test module for **Ch1/L2** with `test_glob` `Ch1/L2.py` under `python/fundamentals/` (pytest, co-located with lesson layout); align with spine `depends_on: [Ch1/L1]`; deterministic; no learner implementation; verify with `uv run pytest Ch1/L2.py`.

**Assistant actions:**

- Added [`python/fundamentals/Ch1/L2.py`](python/fundamentals/Ch1/L2.py): mirrors [`Ch1/L1.py`](python/fundamentals/Ch1/L1.py) (`_course_root`, `src/main.py` entrypoint, subprocess `sys.executable`, 10s timeout); asserts exit 0; asserts stdout is a **short multi-line banner** (2–20 non-empty visible lines) matching spine *Build a Simple Banner* / string output shaping—no stdin; no `tests/support/` needed.
- Ran `uv run pytest Ch1/L2.py` from `python/fundamentals/`: **1 passed, 1 failed** on current L1-only `main.py` (single line) — expected until the learner implements the banner.

---

## 2026-03-28 — Marsh Ch1/L2 lesson (`Ch1/L2.md`)

**User request:** Write `python/fundamentals/Ch1/L2.md` for *Build a Simple Banner*; no `Ch1/L2.hints.md` (`hints: false`); cite spine, overview, repo-root `course/templates/lesson.md` if present, and `Ch1/L2.py`; beginner audience; tasks/checklist match tests; verification `uv run pytest Ch1/L2.py`; no step-by-step solution in the main lesson.

**Assistant actions:**

- Added [`python/fundamentals/Ch1/L2.md`](python/fundamentals/Ch1/L2.md): cited [`python/fundamentals/course/spine.yaml`](python/fundamentals/course/spine.yaml), [`python/fundamentals/course/overview.md`](python/fundamentals/course/overview.md), [`course/templates/lesson.md`](course/templates/lesson.md), [`python/fundamentals/Ch1/L2.py`](python/fundamentals/Ch1/L2.py); concept (literals, concatenation, multi-line banner vs L1); same `src/main.py` entrypoint; acceptance checklist aligned with exit 0, 2–20 lines, every line visible; `uv run pytest Ch1/L2.py`; misconceptions (blank lines, line cap, vs L1 single line); footer notes no hints file.

---

## 2026-03-28 — Marsh rule: optional Concept code

**User request:** Implement plan “Marsh concept code examples”: allow Marsh to optionally provide very basic code **only** in the Concept section; update template and Maestro Marsh constraints; do not edit the plan file.

**Assistant actions:**

- Updated [`.cursor/rules/marsh-lesson-author.mdc`](.cursor/rules/marsh-lesson-author.mdc): frontmatter description; expanded **Concept** output bullet; pedagogy bullet for optional Concept-only snippets + tasks stay non-recipe; forbidden list clarifier for tiny illustrations; session checklist item for Concept-only minimal code.
- Updated [`course/templates/lesson.md`](course/templates/lesson.md): Concept placeholder allows optional single short illustrative example with same guardrails.
- Updated [`.cursor/rules/maestro-orchestrator.mdc`](.cursor/rules/maestro-orchestrator.mdc): Marsh block constraints mention optional minimal illustrative code only under Concept.

---

## 2026-03-28 — Marsh Ch1/L2 lesson update (`Ch1/L2.md`)

**User request:** Update `python/fundamentals/Ch1/L2.md` for *Build a Simple Banner* with the same citations/constraints as prior Marsh brief (spine, overview, `python/fundamentals/course/templates/lesson.md` if present, `Ch1/L2.py`); beginner audience; tasks/checklist match tests; `uv run pytest Ch1/L2.py`; no hints file.

**Assistant actions:**

- Revised [`python/fundamentals/Ch1/L2.md`](python/fundamentals/Ch1/L2.md): expanded **Cited materials** (spine includes `depends_on`; note that `python/fundamentals/course/templates/lesson.md` is absent and [`course/templates/lesson.md`](course/templates/lesson.md) at repo root defines section shape); concept paragraphs slightly simpler; line-split explanation tied to test code; acceptance bullet references per-line `strip` rule; full path for spec file; verification unchanged.

---

## 2026-03-28 — User `done` after Ch1/L2

**User request:** `done` (lesson complete).

**Assistant actions:**

- Confirmed `uv run pytest Ch1/L2.py` passes from `python/fundamentals/`.
- Set [`python/fundamentals/course/progress.yaml`](python/fundamentals/course/progress.yaml) to `last_completed: Ch1/L2`, `next_target: Ch1/L3`.
- Routed **Ch1/L3** Riley/Marsh prompts (*Comment What Your Script Does*, `Ch1/L3.py`, `depends_on: [Ch1/L2]`, `hints: false`).

---

## 2026-03-28 — User `done` after Ch1/L3

**User request:** `done` (Ch1/L3 complete).

**Assistant actions:**

- Ran `uv run pytest Ch1/L3.py` from `python/fundamentals/` — all passed.
- Set [`python/fundamentals/course/progress.yaml`](python/fundamentals/course/progress.yaml) to `last_completed: Ch1/L3`, `next_target: Ch2/L1`.
- Routed **Ch2/L1** Riley/Marsh (*Remember Values with Variables*, `Ch2/L1.py`, `depends_on: [Ch1/L3]`, `hints: false`).

---

## 2026-03-28 — Marsh Ch1/L3 lesson (`Ch1/L3.md`)

**User request:** Author `python/fundamentals/Ch1/L3.md` only (no hints); cite spine, overview, repo-root `course/templates/lesson.md`, `Ch1/L3.py`; no recipe in Assigned tasks; optional tiny Concept snippet per Marsh rule; match tests; `uv run pytest Ch1/L3.py`.

**Assistant actions:**

- Added [`python/fundamentals/Ch1/L3.md`](python/fundamentals/Ch1/L3.md): title *Comment What Your Script Does* per [`CONTENTS.md`](python/fundamentals/CONTENTS.md); cited materials block; **Concept** (comments for humans, L2 banner preserved) plus one generic `#` example (not a solution); **Assigned task(s)** outcome-focused (two full-line `#` bodies, length ≥8, banner+study/log vocabulary per `Ch1/L3.py`); acceptance checklist aligned with exit 0, 2–20 visible banner lines, comment-body rules and regex themes; runner `uv run pytest Ch1/L3.py`; misconceptions (short comments, inline vs full-line, one-line banner); `hints: false` footer. Ran `uv run pytest Ch1/L3.py`: 2 passed, 1 failed on current `main.py` missing comments (expected until learner completes L3).

---

## 2026-03-28 — Riley Ch1/L3 tests (`Ch1/L3.py`)

**User request:** Add only the test module for **Ch1/L3** with `test_glob` `python/fundamentals/Ch1/L3.py`; align with [`python/fundamentals/course/spine.yaml`](python/fundamentals/course/spine.yaml) (*Comment What Your Script Does*, comments + banner/study-log explanation), [`python/fundamentals/course/overview.md`](python/fundamentals/course/overview.md) and [`course/guides/test-authoring/pytest.md`](course/guides/test-authoring/pytest.md); honor `depends_on: [Ch1/L2]` via [`python/fundamentals/Ch1/L2.py`](python/fundamentals/Ch1/L2.py)-style runtime banner checks; deterministic; no shared fixtures beyond this file; no learner implementation; verify `uv run pytest Ch1/L3.py`.

**Assistant actions:**

- Added [`python/fundamentals/Ch1/L3.py`](python/fundamentals/Ch1/L3.py): same subprocess/`src/main.py` harness as L2; `test_running_program_exits_successfully`; `test_running_program_prints_short_multiline_banner` (2–20 non-empty visible lines); `test_main_script_has_full_line_comments_about_banner_and_study_log` (≥2 full-line `#` bodies, each ≥8 chars; combined text must match banner/output vocabulary and study/log vocabulary via regex). Footer: `uv run pytest Ch1/L3.py`. Ran verification: **3 collected**, **1 failed** on sample `main.py` missing comments (expected until L3 completion); no edits under `src/`.

---

## 2026-03-28 — Riley: write tests only (no runner obligation)

**User request:** Riley should not need to run anything—just write the test.

**Assistant actions:**

- Updated [`.cursor/rules/kwon-test-architect.mdc`](.cursor/rules/kwon-test-architect.mdc): new **Execution** section (deliverable is the test file; no pytest/vitest/npm unless user asks); session checklist item reworded to “would collect/run only this lesson” without requiring Riley to run it.
- Updated Riley checklists in [`course/guides/test-authoring/pytest.md`](course/guides/test-authoring/pytest.md), [`vitest.md`](course/guides/test-authoring/vitest.md), and [`jest.md`](course/guides/test-authoring/jest.md) for the same split: author tests; running the stack is optional / for others.

---

## 2026-03-28 — Documentation: `uv run pytest` (uv) everywhere

**User request:** We are now using **uv**; update any documentation that showed bare `pytest` to **`uv run pytest`**.

**Assistant actions:**

- [`course/guides/test-authoring/pytest.md`](course/guides/test-authoring/pytest.md): canonical runner is **`uv run pytest`**; Riley checklist uses the same; optional non-uv fallback noted for other repos.
- [`.cursor/rules/kwon-test-architect.mdc`](.cursor/rules/kwon-test-architect.mdc): per-lesson example, footer hint, **Execution** section, and session checklist aligned with **`uv run pytest`** for uv-managed Python.
- [`course/templates/lesson.md`](course/templates/lesson.md), [`course/spine-and-contents.md`](course/spine-and-contents.md), [`ORIGINAL_PLAN.plan.md`](ORIGINAL_PLAN.plan.md): example commands updated.
- [`python/fundamentals/course/overview.md`](python/fundamentals/course/overview.md), [`python/fundamentals/course/glossary.md`](python/fundamentals/course/glossary.md), [`python/fundamentals/ATLAS_PROMPT.md`](python/fundamentals/ATLAS_PROMPT.md): learner and Atlas copy use **`uv run pytest`** only (no bare `pytest` in learner-facing docs).
- [`course/guides/test-authoring/README.md`](course/guides/test-authoring/README.md): one-line pointer to **`uv run pytest`** for Python in this workspace.

---

## 2026-03-28 — uv project docs: `uv sync` / `uv add` (not `pip install`)

**User request:** Documentation pass for an **uv** (“ultraviolet”) project—e.g. **`pip install`** should read as **`uv add`**.

**Assistant actions:**

- [`python/fundamentals/README.md`](python/fundamentals/README.md): **`uv sync`**, **`uv add`** / **`uv add --dev`** / **`uv remove`**, plus existing **`uv run pytest`**.
- [`python/fundamentals/course/overview.md`](python/fundamentals/course/overview.md): prerequisites + **Test stack** bullets for **`uv sync`**, **`uv add`**, **`uv remove`**; discourage **`pip install` / `requirements.txt`** for this repo.
- [`course/guides/test-authoring/pytest.md`](course/guides/test-authoring/pytest.md): new **Dependencies (uv projects)** section; pitfalls updated for uv vs pip.
- [`course/guides/test-authoring/README.md`](course/guides/test-authoring/README.md), [`README.md`](README.md) (repo root): pointers to uv workflow.
- [`python/fundamentals/ATLAS_PROMPT.md`](python/fundamentals/ATLAS_PROMPT.md): **`uv sync`** and **`uv add`** in the post-init note.
- [`python/fundamentals/course/glossary.md`](python/fundamentals/course/glossary.md): **uv** term.
- [`.cursor/rules/kwon-test-architect.mdc`](.cursor/rules/kwon-test-architect.mdc): **`uv add`** vs **`pip install`** in inputs.

---

## 2026-03-28 — `python/<slug>/` + uv init for new Python courses

**User request:** Future Python projects should automatically live in a **new directory under `python/`**, use **uv**; **Atlas** may run **`uv init`** when needed.

**Assistant actions:**

- Added [`python/README.md`](python/README.md): one folder per course, uv-only workflow, **`uv init`** / **`uv add pytest`** for new slugs, layout aligned with `python/fundamentals/`, spine validates vs root schema.
- Updated [`.cursor/rules/atlas-learning-architect.mdc`](.cursor/rules/atlas-learning-architect.mdc): **Python courses in this workspace** section; globs for `python/**/course/spine.yaml`, `CONTENTS.md`, `overview.md`.
- Updated [`.cursor/rules/kwon-test-architect.mdc`](.cursor/rules/kwon-test-architect.mdc) and [`.cursor/rules/marsh-lesson-author.mdc`](.cursor/rules/marsh-lesson-author.mdc): globs include **`python/**/Ch*/L*.{py,md,…}`** for nested courses.
- Updated [`.cursor/rules/maestro-orchestrator.mdc`](.cursor/rules/maestro-orchestrator.mdc): monorepo note to cite **`@python/<slug>/…`** when spine/progress live under **`python/`**.
- Updated [`README.md`](README.md) (repo root), [`python/fundamentals/ATLAS_PROMPT.md`](python/fundamentals/ATLAS_PROMPT.md), [`course/guides/test-authoring/pytest.md`](course/guides/test-authoring/pytest.md) to point at the convention.

---

## 2026-03-28 — User `done` after Ch2/L1

**User request:** `done` (Ch2/L1 complete).

**Assistant actions:**

- Ran `uv run pytest Ch2/L1.py` from `python/fundamentals/` — all passed.
- Set [`python/fundamentals/course/progress.yaml`](python/fundamentals/course/progress.yaml) to `last_completed: Ch2/L1`, `next_target: Ch2/L2`.
- Routed **Ch2/L2** Riley/Marsh (*Read a Line from the Keyboard*, `Ch2/L2.py`, `depends_on: [Ch2/L1]`, `hints: false`).

---

## 2026-03-29 — Riley Ch2/L1 tests (`Ch2/L1.py`)

**User request:** Add only the test module for **Ch2/L1** (`test_glob` `python/fundamentals/Ch2/L1.py`); align with [`python/fundamentals/course/spine.yaml`](python/fundamentals/course/spine.yaml) (*Remember Values with Variables*, string variables for app title and default log filename), [`python/fundamentals/course/overview.md`](python/fundamentals/course/overview.md), [`course/guides/test-authoring/pytest.md`](course/guides/test-authoring/pytest.md); `depends_on: [Ch1/L3]` per [`python/fundamentals/Ch1/L3.py`](python/fundamentals/Ch1/L3.py) (subprocess smoke only—no full L3 re-test); deterministic; no shared fixtures; no learner implementation; verify `uv run pytest Ch2/L1.py`.

**Assistant actions:**

- Added [`python/fundamentals/Ch2/L1.py`](python/fundamentals/Ch2/L1.py): `main_script` fixture + `_run_entrypoint` (same cwd/`src/main.py` pattern as Ch1); `test_running_program_exits_successfully`; `test_main_defines_distinct_title_and_log_filename_variables` parses `main.py` with `ast`, collects simple `AnnAssign`/`Assign` string literals anywhere in the tree, requires a **title-ish** name with a non-filename-like title string and a **log-file-ish** name with a value ending in `.<ext>`, and **disjoint** variable names. Footer: `uv run pytest Ch2/L1.py`. Ran **`uv run pytest Ch2/L1.py`**: **2 tests**, **1 failed** on current `main.py` (no qualifying string literal assignments yet—expected until the learner implements Ch2/L1).

---

## 2026-03-29 — Marsh Ch2/L1 lesson (`Ch2/L1.md`)

**User request:** Author `python/fundamentals/Ch2/L1.md` only (no hints); cite spine, overview, repo-root `course/templates/lesson.md`, `Ch2/L1.py`; no recipe in Assigned tasks; optional tiny Concept snippet per Marsh rule; align with tests; `uv run pytest Ch2/L1.py`.

**Assistant actions:**

- Added [`python/fundamentals/Ch2/L1.md`](python/fundamentals/Ch2/L1.md): title *Remember Values with Variables*; cited materials; **Concept** (variables, assignment, title vs log filename) + one generic assignment snippet; outcome-only **Assigned task(s)** (patterns for title vs filename variables per `Ch2/L1.py`); acceptance checklist (exit 0, parseable `main.py`, AST string-literal rules, disjoint names); runner `uv run pytest Ch2/L1.py`; misconceptions; `hints: false` footer. Ran **`uv run pytest Ch2/L1.py`**: **1 passed**, **1 failed** on current `main.py` (no qualifying literal assignments yet—expected until learner completes Ch2/L1).

---

## 2026-03-28 — Lesson markdown: drop cited block

**User request:** Remove the cited section from lesson markdowns.

**Assistant actions:**

- Removed the **Cited materials** block (spine/overview/template/test links) from [`python/fundamentals/Ch1/L2.md`](python/fundamentals/Ch1/L2.md), [`python/fundamentals/Ch1/L3.md`](python/fundamentals/Ch1/L3.md), and [`python/fundamentals/Ch2/L1.md`](python/fundamentals/Ch2/L1.md). [`python/fundamentals/Ch1/L1.md`](python/fundamentals/Ch1/L1.md) and [`course/templates/lesson.md`](course/templates/lesson.md) were already without that section.

---

## 2026-03-28 — Marsh rule vs “Cited materials”

**User request:** Whether something in Marsh’s rule causes the cited section.

**Assistant answer (logged):** [`.cursor/rules/marsh-lesson-author.mdc`](.cursor/rules/marsh-lesson-author.mdc) does not require or name **Cited materials**; it requires cross-linking the test file (spec) and following the lesson template. The cited block was likely from user prompts (e.g. “cite spine, overview…”) or model habit, not the Marsh rule text.

---

## 2026-03-28 — Maestro / Riley / Marsh: progress-first handoffs

**User request:** Drop Maestro “cite …” style return prompts; have Riley (Kwon) and Marsh resolve the current lesson from `course/progress.*`.

**Assistant actions:**

- Updated [`.cursor/rules/maestro-orchestrator.mdc`](.cursor/rules/maestro-orchestrator.mdc): **Target lesson** resolution from `next_target` → next after `last_completed` → first spine lesson; batch override when the paste block lists multiple `Chk/Ln`; Riley/Marsh templates use **Context:** (`@…/progress`, spine, overview) instead of “Cite attachments”; Marsh constraint forbids a **Cited materials** block; session checklist aligns with progress-first prompts.
- Updated [`.cursor/rules/kwon-test-architect.mdc`](.cursor/rules/kwon-test-architect.mdc): inputs + session checklist require reading **`course/progress.*`** and resolving **`Chk/Ln`** before the spine row.
- Updated [`.cursor/rules/marsh-lesson-author.mdc`](.cursor/rules/marsh-lesson-author.mdc): same progress resolution; **Forbidden**: separate Cited materials section; wording “state the command” instead of “cite the command.”

---

## 2026-03-29 — New Python course: data structures (scaffold + Atlas)

**User request:** Maestro: new Python project on data structures.

**Assistant actions:**

- **Maestro routing:** No spine yet — **Atlas only** (no Riley/Marsh).
- Created [`python/data-structures/`](python/data-structures/): **`uv init --no-readme`**, **`uv add pytest`**, **`uv sync`**.
- Added [`python/data-structures/README.md`](python/data-structures/README.md) — pointer to layout, **`uv run pytest`**, fundamentals/schema links.
- Added [`python/data-structures/ATLAS_PROMPT.md`](python/data-structures/ATLAS_PROMPT.md) — Atlas paste block: outputs under `python/data-structures/`, validate vs `@course/spine.schema.json`, capstone DS course, uv/pytest, `course/progress.yaml` starter, Maestro paths for follow-on.

---

## 2026-03-29 — Maestro: data-structures start (Ch1/L1)

**User request:** Maestro with `@python/data-structures/course/progress.yaml` and `@python/data-structures/course/spine.yaml`.

**Assistant actions:**

- Resolved target **Ch1/L1** (*Represent Documents as a Sequenced Corpus*) — `last_completed: null`, no `next_target`; first spine lesson. `test_glob: Ch1/L1.py`, `depends_on: []`, `hints: false`.
- Emitted **progress** snippet (optional `next_target: Ch1/L1`), **Riley** and **Marsh** paste blocks with `@python/data-structures/…` paths and progress-first resolution.

---

## 2026-03-29 — Ch2/L3 next lesson (tests + Marsh)

**User request:** “Next lesson, please.” [`python/fundamentals/course/progress.yaml`](python/fundamentals/course/progress.yaml) already had `last_completed: Ch2/L2`, `next_target: Ch2/L3`.

**Assistant actions:**

- Added [`python/fundamentals/Ch2/L3.py`](python/fundamentals/Ch2/L3.py): subprocess stdin + AST for *Choose What Happens Next*: padded non-empty note still echoed trimmed; whitespace-only stdin needs a real **rejection** line on stdout (regex avoids matching **Enter** in `input()` prompts); `main.py` must have **`if` + `orelse`**, one **`input`**, and **`.strip()`**.
- Added [`python/fundamentals/Ch2/L3.md`](python/fundamentals/Ch2/L3.md): Marsh-style lesson (CONTENTS title); optional Concept snippet only; `hints: false`; evidence `python/fundamentals/Ch2/L3.py`; `uv run pytest Ch2/L3.py`.
- Ran **`uv run pytest Ch2/L3.py`**: **1 passed, 2 failed** on current [`src/main.py`](python/fundamentals/src/main.py) until L3 branching + rejection message are implemented.

---

## 2026-03-29 — Riley Ch2/L2 tests (`Ch2/L2.py`)

**User request:** Riley (kwon-test-architect): only [`python/fundamentals/Ch2/L2.py`](python/fundamentals/Ch2/L2.py) for *Read a Line from the Keyboard* (`input`, prompt, `strip`); context from [`python/fundamentals/course/progress.yaml`](python/fundamentals/course/progress.yaml) (`next_target: Ch2/L2`), spine, overview, pytest guide; [`python/fundamentals/Ch2/L1.py`](python/fundamentals/Ch2/L1.py) pattern; deterministic; no learner `src/` edits; verify `uv run pytest Ch2/L2.py`.

**Assistant actions:**

- Added [`python/fundamentals/Ch2/L2.py`](python/fundamentals/Ch2/L2.py): `_run_with_stdin` against `src/main.py`; `test_output_shows_stripped_note_not_padding_secret` (fed padded unique token + newline; assert exit 0, token appears on stdout, full padded string does not—`strip` contract); `test_main_source_calls_input_once_with_prompt_and_uses_strip` (`ast` parse: exactly one `input(...)` call with a prompt via args or keywords; source contains a `.strip()` call). Dropped a weaker “exit 0 + stdin” test that passed when stdin was ignored. Footer: `uv run pytest Ch2/L2.py`. Ran **`uv run pytest Ch2/L2.py`**: **2 tests**, **2 failed** on current [`main.py`](python/fundamentals/src/main.py) (no `input`/`strip` yet—expected until Ch2/L2 implementation).

---

## 2026-03-29 — Marsh Ch2/L2 lesson (`Ch2/L2.md`)

**User request:** “lesson 2” (interpreted as Chapter 2, lesson 2—*Read a Line from the Keyboard*).

**Assistant actions:**

- Added [`python/fundamentals/Ch2/L2.md`](python/fundamentals/Ch2/L2.md): matches streamlined Ch2 lesson style (no Cited block); **Concept** (`input`, prompt, `strip`) + tiny illustrative snippet; outcome-focused **Assigned task(s)**; acceptance aligned with [`Ch2/L2.py`](python/fundamentals/Ch2/L2.py); `uv run pytest Ch2/L2.py`; misconceptions; `hints: false` footer. Ran **`uv run pytest Ch2/L2.py`**: **2 failed** on current `main.py` until learner implements one `input`, prompt, `strip`, and prints stripped note.

---

## 2026-03-29 — User `done` after Ch2/L2

**User request:** `done` (Ch2/L2 complete).

**Assistant actions:**

- Ran `uv run pytest Ch2/L2.py` from `python/fundamentals/` — all passed.
- Set [`python/fundamentals/course/progress.yaml`](python/fundamentals/course/progress.yaml) to `last_completed: Ch2/L2`, `next_target: Ch2/L3`.
- Routed **Ch2/L3** Riley/Marsh (*Choose What Happens Next*, `Ch2/L3.py`, `depends_on: [Ch2/L2]`, `hints: false`).

---

## 2026-03-28 — Atlas: python/data-structures spine + course artifacts

**User request:** Plan a full Python **data structures** course under `python/data-structures/`: `course/spine.yaml` (validate vs repo `course/spine.schema.json`), `CONTENTS.md`, `course/overview.md`, optional glossary, `course/progress.yaml` (`last_completed: null`); one capstone; `test_glob` per lesson = that lesson only; `depends_on` DAG; hints only where warranted; no full `Chk/Ln.md`, test files, or learner implementation.

**Assistant actions:**

- Added [`python/data-structures/course/spine.yaml`](python/data-structures/course/spine.yaml): capstone **in-memory search index** (corpus → scan → stack/queue/deque → inverted index + sets → BST + trie → heap top-k → adjacency graph + BFS/DFS); 19 lessons; linear `depends_on` chain; `hints: true` on Ch2/L2, Ch3/L3, Ch4/L3, Ch5/L1, Ch6/L2, Ch6/L3.
- Added [`python/data-structures/CONTENTS.md`](python/data-structures/CONTENTS.md) mirroring spine titles/order.
- Added [`python/data-structures/course/overview.md`](python/data-structures/course/overview.md): behavioral end state, prerequisites (Python basics), uv/pytest/`src/` notes.
- Added [`python/data-structures/course/glossary.md`](python/data-structures/course/glossary.md).
- Added [`python/data-structures/course/progress.yaml`](python/data-structures/course/progress.yaml) with `last_completed: null`.
- Validated spine and progress with `jsonschema` + PyYAML against repository schemas (OK).

---

## 2026-03-29 — Riley data-structures Ch1/L1 (`Ch1/L1.py`)

**User request:** Per kwon-test-architect: only tests for **Ch1/L1** (`test_glob` `Ch1/L1.py` under `python/data-structures/`); deterministic; scoped run collects only this lesson (+ path setup in file); no learner implementation in `src/`. Context: [`python/data-structures/course/progress.yaml`](python/data-structures/course/progress.yaml), [`course/spine.yaml`](python/data-structures/course/spine.yaml), [`course/overview.md`](python/data-structures/course/overview.md).

**Assistant actions:**

- Added [`python/data-structures/Ch1/L1.py`](python/data-structures/Ch1/L1.py): prepends `src/` on `sys.path`; imports learner module **`corpus`** exposing **`build_corpus(documents)`** and **`get_document_text(corpus, doc_id)`**; tests cover list order + stable ids, retrieval, **ValueError** on duplicate ids, **KeyError** on unknown id, defensive copy of input list, independence from caller replacing tuple slots. Footer: `uv run pytest Ch1/L1.py`. Ran collection: errors until [`src/corpus.py`](python/data-structures/src/corpus.py) exists (expected).

---

## 2026-03-29 — Marsh data-structures Ch1/L1 (`Ch1/L1.md`)

**User request:** Author [`python/data-structures/Ch1/L1.md`](python/data-structures/Ch1/L1.md) for *Represent Documents as a Sequenced Corpus*; resolve `Chk/Ln` from [`progress.yaml`](python/data-structures/course/progress.yaml) + spine (`hints: false`); context spine/overview/template/tests; no step-by-step in Assigned tasks; optional minimal Concept code only; follow [`course/templates/lesson.md`](course/templates/lesson.md); no **Cited materials** section.

**Assistant actions:**

- Added [`python/data-structures/Ch1/L1.md`](python/data-structures/Ch1/L1.md): title matches [`CONTENTS.md`](python/data-structures/CONTENTS.md); **Concept** (ordered list, stable ids, id+text pairs) + tiny list-of-tuples snippet; **Assigned task(s)** for `src/corpus.py`, `build_corpus`, `get_document_text` (outcomes/errors, no recipe); acceptance aligned with all six tests in [`Ch1/L1.py`](python/data-structures/Ch1/L1.py); runner `uv run pytest Ch1/L1.py` from `python/data-structures/`; misconceptions (list vs dict-only corpus, `ValueError`/`KeyError`, aliasing); `hints: false` footer. Ran pytest: **import errors** until learner adds `corpus` module (expected).

---

## 2026-03-29 — User `done` data-structures Ch1/L1

**User request:** `done` (Ch1/L1 complete).

**Assistant actions:**

- Ran `uv run pytest Ch1/L1.py` from `python/data-structures/` — **6 passed**.
- Updated [`python/data-structures/course/progress.yaml`](python/data-structures/course/progress.yaml) to `last_completed: Ch1/L1`, `next_target: Ch1/L2`.
- Routed **Ch1/L2** Riley/Marsh (*Walk the Corpus with Control*, `Ch1/L2.py`, `depends_on: [Ch1/L1]`, `hints: false`).

---

## 2026-03-29 — Riley data-structures Ch1/L2 (`Ch1/L2.py`)

**User request:** Only tests for **Ch1/L2** (`test_glob` `Ch1/L2.py` under `python/data-structures/`); resolve from [`python/data-structures/course/progress.yaml`](python/data-structures/course/progress.yaml) (`next_target: Ch1/L2`); context spine/overview; `depends_on: [Ch1/L1]` / [`Ch1/L1.py`](python/data-structures/Ch1/L1.py); deterministic; scoped run; no learner implementation in `src/`.

**Assistant actions:**

- Added [`python/data-structures/Ch1/L2.py`](python/data-structures/Ch1/L2.py): same `src/` `sys.path` setup as L1; fixture imports **`corpus`** and requires **`summarize_corpus(corpus)`** returning **`(document_count, body_lengths, total_characters)`** (lengths in **list order**); tests for empty corpus, multibody stats + `total == sum(lengths)`, **order-sensitive** length runs vs swapped rows, and **AST** check that **`enumerate(...)`** appears in `src/corpus.py`. Footer: `uv run pytest Ch1/L2.py`. Ran pytest: **fixture fails** until `summarize_corpus` exists (expected); fixed a stray space in a test function name that broke collection.

---

## 2026-03-29 — Marsh data-structures Ch1/L2 (`Ch1/L2.md`)

**User request:** Author [`python/data-structures/Ch1/L2.md`](python/data-structures/Ch1/L2.md) for *Walk the Corpus with Control*; resolve `Chk/Ln` like Riley (`next_target: Ch1/L2` in [`progress.yaml`](python/data-structures/course/progress.yaml)); `hints: false`; no cited block; no step-by-step Assigned tasks; optional minimal Concept code only.

**Assistant actions:**

- Added [`python/data-structures/Ch1/L2.md`](python/data-structures/Ch1/L2.md): **Concept** (ordered traversal, `for`, `enumerate`, summary stats) + tiny illustrative loop; **Assigned task(s)** extend `src/corpus.py` with **`summarize_corpus`** return shape and ordered walk (warn against dict-order summaries); acceptance mapped to all four tests in [`Ch1/L2.py`](python/data-structures/Ch1/L2.py); runner `uv run pytest Ch1/L2.py`; misconceptions; `hints: false` footer. Ran pytest: errors until **`summarize_corpus`** implemented (expected on current `corpus.py`).

---

## 2026-03-29 — Rewrite Ch1/L2 tests behavior-first

**User request:** Implement to-do `rewrite-l2-test-contracts`: refactor [`python/data-structures/Ch1/L2.py`](python/data-structures/Ch1/L2.py) to behavior-first `summarize_corpus` contracts (remove implementation-coupled AST/`enumerate` checks).

**Assistant actions:**

- Updated [`python/data-structures/Ch1/L2.py`](python/data-structures/Ch1/L2.py): removed AST/source-inspection helpers and `test_corpus_module_calls_enumerate_somewhere`.
- Kept import wiring/fixture shape, but moved `summarize_corpus` presence out of fixture into dedicated `test_corpus_exposes_summarize_corpus_callable` for clearer diagnostics.
- Added behavior-first contract checks: parameterized empty + mixed corpus cases; exact tuple contract (`len == 3`), count/length/total invariants, and explicit order-sensitive swapped-corpus test.
- Added `test_summarize_corpus_does_not_mutate_input_corpus` as safe extension.
- Added helper gating so when `summarize_corpus` is missing you get one contract failure and behavior tests skip (instead of repeated setup-style failures).
- Ran `uv run pytest Ch1/L2.py` from `python/data-structures/`: **1 failed, 5 skipped** (expected until learner adds `summarize_corpus`).

---

## 2026-03-28 — Complete to-do `remove-enumerate-ast-check`

**User request:** Implement assigned to-do `remove-enumerate-ast-check` (delete source-inspection enumerate test and replace with order-behavior checks) from attached rewrite plan; do not edit plan file.

**Assistant actions:**

- Reviewed [`python/data-structures/Ch1/L2.py`](python/data-structures/Ch1/L2.py) and confirmed the implementation-coupled AST/enumerate inspection test is already removed.
- Verified behavior-first order semantics are present via `test_length_sequence_follows_corpus_sequence_not_just_multiset` and contract assertions for tuple shape/counts/length totals.
- Searched lesson tests under `python/data-structures/Ch1/` to confirm no residual `ast`/`enumerate` source-inspection checks remain for this lesson.
- No additional test-file edits were required for this to-do; plan file remained unchanged.

---

## 2026-03-28 — Complete to-do `optional-rule-note`

**User request:** Implement assigned to-do `optional-rule-note`: add optional guidance in [`.cursor/rules/kwon-test-architect.mdc`](.cursor/rules/kwon-test-architect.mdc) discouraging implementation-coupled source inspection; do not edit the attached plan file.

**Assistant actions:**

- Updated [`.cursor/rules/kwon-test-architect.mdc`](.cursor/rules/kwon-test-architect.mdc) under **Principles** with a behavior-first guardrail: prefer behavior assertions over source-inspection checks (AST/regex), except when a lesson explicitly teaches syntax form and behavior cannot express it fairly.
- Left the plan file unchanged.

---

## 2026-03-28 — Complete to-dos `unify-target-resolution` and `add-rule-guardrails`

**User request:** Implement assigned to-dos from the attached rule/project audit plan: (1) unify repeated `Chk/Ln` target-resolution logic and reference it from Maestro/Riley/Marsh, and (2) add precedence/conflict and handoff contract sections to all role rules. Do not edit the plan file itself.

**Assistant actions:**

- Added a new canonical shared rule section at [`.cursor/rules/shared-target-resolution.mdc`](.cursor/rules/shared-target-resolution.mdc) defining one `Chk/Ln` resolution contract (explicit list override, `next_target`, next after `last_completed`, and first-lesson start behavior).
- Refactored [`.cursor/rules/maestro-orchestrator.mdc`](.cursor/rules/maestro-orchestrator.mdc), [`.cursor/rules/kwon-test-architect.mdc`](.cursor/rules/kwon-test-architect.mdc), and [`.cursor/rules/marsh-lesson-author.mdc`](.cursor/rules/marsh-lesson-author.mdc) to reference the shared canonical contract instead of repeating per-file resolution logic.
- Added **Conflict precedence (hard)** and **Role handoff contract** sections to all role rules: [`.cursor/rules/maestro-orchestrator.mdc`](.cursor/rules/maestro-orchestrator.mdc), [`.cursor/rules/kwon-test-architect.mdc`](.cursor/rules/kwon-test-architect.mdc), [`.cursor/rules/marsh-lesson-author.mdc`](.cursor/rules/marsh-lesson-author.mdc), and [`.cursor/rules/atlas-learning-architect.mdc`](.cursor/rules/atlas-learning-architect.mdc).
- Updated relevant checklist lines in Maestro/Riley/Marsh rules to reference the shared target-resolution contract.
- Verified no linter diagnostics were introduced for edited rule files.

---

## 2026-03-28 — Complete to-dos `add-validation-automation`, `tighten-templates`, `improve-workflow-docs`

**User request:** Implement assigned to-dos from the attached rule/project audit plan: (1) add repo validation automation, (2) tighten lesson/hints templates with concrete examples and hint-depth boundaries, and (3) update README docs with bootstrap/governance/batching guidance. Do not edit the plan file.

**Assistant actions:**

- Added [`scripts/validate_repo.py`](scripts/validate_repo.py): repo-level validator that discovers course roots via `course/spine.*`, validates spine/progress against [`course/spine.schema.json`](course/spine.schema.json) and [`course/progress.schema.json`](course/progress.schema.json), checks spine/`CONTENTS.md` chapter+lesson title/order parity, and checks per-lesson `test_glob` scoping to lesson-local targets.
- Updated [`course/templates/lesson.md`](course/templates/lesson.md) with concrete "good vs bad" examples for `Concept`, `Assigned task(s)`, and `Acceptance criteria`, plus explicit test-mappability guidance.
- Updated [`course/templates/lesson-hints.md`](course/templates/lesson-hints.md) with a depth rubric (Levels 1-3), explicit "not allowed" boundary for full solutions, and nudge quality examples.
- Updated root [`README.md`](README.md) with a new-course bootstrap + preflight section, governance rules for when to replan with Atlas vs continue Riley/Marsh flow, and Maestro batch-size guidance (1-3 lessons).
- Updated [`python/README.md`](python/README.md) with a copy-paste bootstrap command sequence and compact governance/batching guidance for day-to-day Python course flow.
- Ran `python3 scripts/validate_repo.py`: exits successfully (`OK: validated 3 course root(s)`), with warnings only for intentionally ungenerated future lesson test files and missing root `CONTENTS.md` for the repository template root.
- Checked diagnostics with `ReadLints` for all edited files; no linter errors reported.

---

## 2026-03-28 — Complete to-dos `adopt-main-test-flow` and `define-selector-contract`

**User request:** Implement assigned to-dos from the attached rule/project audit plan: (1) adopt module-root `main.py` plus append-only `main_test.py` flow with per-lesson selectors across Atlas/Riley/Marsh/Maestro plus schema/docs, and (2) choose and codify one selector mechanism (`-k` or pytest markers) for lesson-scoped execution.

**Assistant actions:**

- Standardized on **pytest markers** for lesson scoping, with canonical naming `lesson_ch<chapter>_l<lesson>` and runner shape `uv run pytest main_test.py -m <lesson_selector>`.
- Updated [`course/spine.schema.json`](course/spine.schema.json): added `lesson_selector` with naming pattern and conditional requirement when `test_glob` is `main_test.py`; expanded `test_glob` docs for migration compatibility.
- Updated [`scripts/validate_repo.py`](scripts/validate_repo.py): added selector validation + duplicate detection for `main_test.py` mode; kept legacy per-lesson file checks but now emits migration warnings (`Ch#/L#.py` -> `main_test.py` + `lesson_selector`).
- Updated role rules to align handoffs and constraints with the new contract: [`.cursor/rules/atlas-learning-architect.mdc`](.cursor/rules/atlas-learning-architect.mdc), [`.cursor/rules/kwon-test-architect.mdc`](.cursor/rules/kwon-test-architect.mdc), [`.cursor/rules/marsh-lesson-author.mdc`](.cursor/rules/marsh-lesson-author.mdc), [`.cursor/rules/maestro-orchestrator.mdc`](.cursor/rules/maestro-orchestrator.mdc), and [`.cursor/rules/shared-target-resolution.mdc`](.cursor/rules/shared-target-resolution.mdc).
- Updated templates and docs to codify the selector contract and command examples: [`course/templates/lesson.md`](course/templates/lesson.md), [`course/templates/lesson-hints.md`](course/templates/lesson-hints.md), [`README.md`](README.md), [`python/README.md`](python/README.md), [`course/guides/test-authoring/README.md`](course/guides/test-authoring/README.md), [`course/guides/test-authoring/pytest.md`](course/guides/test-authoring/pytest.md), [`course/spine.yaml`](course/spine.yaml), [`course/spine.example.yaml`](course/spine.example.yaml), [`python/fundamentals/course/overview.md`](python/fundamentals/course/overview.md), [`python/data-structures/course/overview.md`](python/data-structures/course/overview.md), [`python/fundamentals/README.md`](python/fundamentals/README.md), [`python/data-structures/README.md`](python/data-structures/README.md), [`python/fundamentals/ATLAS_PROMPT.md`](python/fundamentals/ATLAS_PROMPT.md), and [`python/data-structures/ATLAS_PROMPT.md`](python/data-structures/ATLAS_PROMPT.md).
- Ran `python3 scripts/validate_repo.py`: success (`OK: validated 3 course root(s)`), with expected migration warnings for existing legacy spines still using `Ch#/L#.py` test targets.
- Checked edited files with `ReadLints`; no linter diagnostics reported.

---

## 2026-03-28 — Complete to-do `add-migration-strategy`

**User request:** Implement assigned to-do from the attached rule/project audit plan: add a migration path from legacy per-lesson tests (`Ch#/L#.py`) to append-only `main_test.py`, including rollback guidance. Do not edit the attached plan file itself.

**Assistant actions:**

- Updated [`README.md`](README.md) with a dedicated migration playbook section: inventory, staged batch migration, validation commands, full cutover, and cleanup guidance.
- Added explicit rollback guidance in [`README.md`](README.md), including batch-only rollback, preserving legacy files until stable cutover, and selector-collision recovery.
- Updated [`python/README.md`](python/README.md) with a Python-course-specific migration strategy from `Ch#/L#.py` to selector-scoped `main_test.py`.
- Added a compact rollback fallback section in [`python/README.md`](python/README.md) describing spine-row reversion and safe temporary return to legacy per-lesson test execution.

---

## 2026-03-28 — Complete to-do `add-test-growth-guardrails`

**User request:** Implement assigned to-do from the attached rule/project audit plan: define guardrails for `main_test.py` growth, including size/performance thresholds and a split strategy (for example chapter-level files). Do not edit the attached plan file.

**Assistant actions:**

- Updated root [`README.md`](README.md) with a new **`main_test.py` growth guardrails** section defining soft/hard size limits, selector-scoped and full-suite performance targets, and a concrete chapter-level split workflow.
- Updated [`python/README.md`](python/README.md) with Python-specific growth thresholds and chapter-file split rules (`main_test_ch<chapter>.py`) while preserving `lesson_selector` scoping.
- Updated [`.cursor/rules/kwon-test-architect.mdc`](.cursor/rules/kwon-test-architect.mdc) so Riley explicitly enforces growth guardrails, allows chapter-level `test_glob` when thresholds are exceeded, and keeps append-only semantics per file scope.
- Ran diagnostics (`ReadLints`) on all edited files; no linter errors reported.

---

## 2026-03-28 — Complete to-do `add-ci-enforcement`

**User request:** Implement assigned to-do from the attached plan: add CI enforcement for schema validation, spine/`CONTENTS.md` parity, selector uniqueness, and protection against accidental deletion/regression of prior lesson tests; do not edit the plan file.

**Assistant actions:**

- Added [`.github/workflows/ci.yml`](.github/workflows/ci.yml) with pull-request CI that installs validator dependencies and runs:
  - `python3 scripts/validate_repo.py` (schema checks, spine/`CONTENTS.md` parity, selector validation/uniqueness)
  - `python3 scripts/check_test_regression.py --base-ref <pull_request.base.sha>` (regression guard)
- Added [`scripts/check_test_regression.py`](scripts/check_test_regression.py), a git-history-aware guardrail that fails CI when:
  - legacy per-lesson test files (`Ch#/L#.py`) are deleted
  - existing `lesson_ch<chapter>_l<lesson>` selectors are removed from touched `main_test*.py` files
  - existing spine lesson selectors are rewritten for already-defined lessons
- Updated [`README.md`](README.md) related-files references to include the new regression script and CI workflow.
- Ran `python3 scripts/validate_repo.py && python3 scripts/check_test_regression.py` locally:
  - `validate_repo.py` succeeded with expected migration warnings for legacy `test_glob` entries
  - `check_test_regression.py` skipped in local workspace because it is not a git checkout (it runs in CI where git history exists)
- Checked edited files with `ReadLints`; no linter diagnostics reported.

---

## 2026-03-28 — Complete to-do `add-worked-example-course`

**User request:** Implement assigned to-do from the attached rule/project audit plan: create a small reference module showing `main.py`, append-only `main_test.py`, lesson selectors, and end-to-end Maestro/Riley/Marsh flow. Do not edit the attached plan file.

**Assistant actions:**

- Added a compact worked example module at [`python/reference-module/`](python/reference-module/) with learner entrypoint [`main.py`](python/reference-module/main.py), append-only selector-scoped tests in [`main_test.py`](python/reference-module/main_test.py), and uv/pytest config in [`pyproject.toml`](python/reference-module/pyproject.toml).
- Added canonical course artifacts for the reference module:
  - [`course/spine.yaml`](python/reference-module/course/spine.yaml) with `test_glob: main_test.py` and lesson selectors `lesson_ch1_l1`, `lesson_ch1_l2`
  - [`course/progress.yaml`](python/reference-module/course/progress.yaml)
  - [`course/overview.md`](python/reference-module/course/overview.md)
  - [`CONTENTS.md`](python/reference-module/CONTENTS.md)
  - lesson files [`Ch1/L1.md`](python/reference-module/Ch1/L1.md), [`Ch1/L2.md`](python/reference-module/Ch1/L2.md)
- Added an explicit end-to-end handoff walkthrough in [`MAESTRO_RILEY_MARSH_FLOW.md`](python/reference-module/MAESTRO_RILEY_MARSH_FLOW.md) showing progress patch shape, Riley append-only test block behavior, Marsh lesson generation behavior, and selector-scoped test commands.
- Updated repo docs to surface the new example: [`python/README.md`](python/README.md) and root [`README.md`](README.md).
- Ran `python3 scripts/validate_repo.py` from repo root: success (`OK: validated 4 course root(s)`), with expected existing migration warnings for legacy per-lesson test layouts in other courses.
- Ran selector-scoped tests in the worked example:
  - `uv run pytest main_test.py -m lesson_ch1_l1` -> 2 passed
  - `uv run pytest main_test.py -m lesson_ch1_l2` -> 2 passed
- Ran `ReadLints` for edited files; no linter diagnostics reported.
