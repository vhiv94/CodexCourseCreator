# Planning prompt — Python data structures (copy-paste)

**Enable rule:** `planning`.

**Context:** Project already scaffolded at `python/data-structures/` with **`uv init --no-readme`**, **`uv add pytest`**, and **`uv sync`**. Do not replace tooling choices in prose without reason. If the planned course keeps tests, keep **pytest** and **`uv run pytest main_test.py -m <lesson_selector>`** as the runner story in `overview.md`.

---

Paste below this line into Composer with the planning rule attached.

---

**Objective:** Design a **full** course on **data structures in Python**. Start by running a short-answer pre-structure assessment before deciding the final course shape. Choose a coherent scope and one **capstone-style arc** so each lesson advances **one** real step. Output **planning artifacts only**: not full lesson markdown, not full test code, and not learner `src/` solutions.

**Paths (repo root = `coursecreator`, all under `python/data-structures/`):**

- `python/data-structures/course/spine.yaml` — validate against `@course/spine.schema.json` at repository root
- `python/data-structures/CONTENTS.md` — `### Chk: ...` headings and per-chapter numbered lesson titles **verbatim** match spine order and titles
- `python/data-structures/course/overview.md` — motivation, behavioral end-state, prerequisites, chapter map; **pytest** + **uv** (`uv sync`, `uv add`, **`uv run pytest main_test.py -m <lesson_selector>`**) per [`course/guides/test-authoring/pytest.md`](../../course/guides/test-authoring/pytest.md); learner code layout (`src/` or as you document)
- Optional `python/data-structures/course/glossary.md` if jargon-heavy
- `python/data-structures/course/progress.yaml` — **`last_completed: null`** (and optional `next_target: null` or first lesson) per `@course/progress.schema.json`

**Audience / topic (user words):** *“New Python project on data structures.”* Assume learners already know Python basics (functions, loops, simple I/O) unless you explicitly target absolute beginners and widen Chapter 1 accordingly. State the choice in `audience_level` and `overview.md`.

**Spine rules:** Each lesson includes an explicit `assignment`, **`depends_on`** is a sensible DAG, and **`hints: true`** appears only where you intend a later `Ln-hint.md`. Add **`test_glob: main_test.py`** with unique **`lesson_selector`** marker naming (`lesson_ch<chapter>_l<lesson>`) only for lessons that should ship tests.

**Assessment convention:** keep `delivery.assessment_format: short_answer`, `prestructure_assessment: true`, and `prechapter_assessments: true`. Before any future chapter lesson batch is written, expect a short-answer `ASSESSMENT.md` step for that chapter.

**Forbidden (this pass):** Per the planning rule, do not write full `Chk/Ln.md`, full test modules, or a complete capstone implementation.

---

## Workflow note

After planning finishes, use next-step routing with **`@python/data-structures/course/progress.yaml`** and **`@python/data-structures/course/spine.yaml`** for lesson-authoring first and optional test-authoring follow-up handoffs.
