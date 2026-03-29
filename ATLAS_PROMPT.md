# Atlas prompt — Python data structures (copy-paste)

**Enable rule:** `atlas-learning-architect`.

**Context:** Project already scaffolded at `python/data-structures/`: **`uv init --no-readme`**, **`uv add pytest`**, **`uv sync`**. Do not replace tooling choices in prose without reason; keep **pytest** and **`uv run pytest main_test.py -m <lesson_selector>`** as the runner story in `overview.md`.

---

Paste below this line into Composer with Atlas attached.

---

**Objective:** Design a **full** course on **data structures in Python** (lists, dicts, sets, tuples, stacks/queues, trees/heaps/graphs as appropriate for the level — you choose a coherent scope). One **capstone-style arc** (e.g. small library, CLI, or simulation) so each lesson advances **one** real step. Output **planning artifacts only** — not full lesson markdown, not full test code, not learner `src/` solutions.

**Paths (repo root = `coursecreator`, all under `python/data-structures/`):**

- `python/data-structures/course/spine.yaml` — validate against `@course/spine.schema.json` at repository root.
- `python/data-structures/CONTENTS.md` — `### Chk: …` headings and per-chapter numbered lesson titles **verbatim** match spine order and titles.
- `python/data-structures/course/overview.md` — motivation, behavioral end-state, prerequisites, chapter map; **pytest** + **uv** (`uv sync`, `uv add`, **`uv run pytest main_test.py -m <lesson_selector>`**) per [`course/guides/test-authoring/pytest.md`](../../course/guides/test-authoring/pytest.md); learner code layout (`src/` or as you document).
- Optional `python/data-structures/course/glossary.md` if jargon-heavy.
- `python/data-structures/course/progress.yaml` — **`last_completed: null`** (and optional `next_target: null` or first lesson) per `@course/progress.schema.json`.

**Audience / topic (user words):** *“New Python project on data structures.”* Assume learners **already know Python basics** (functions, loops, simple I/O) unless you explicitly target absolute beginners and widen Chapter 1 accordingly — state the choice in `audience_level` and `overview.md`.

**Spine rules:** Each lesson uses **`test_glob: main_test.py`** with unique **`lesson_selector`** marker naming (`lesson_ch<chapter>_l<lesson>`), **`depends_on`** is a sensible DAG, and **`hints: true`** appears only where you intend a later `Ln.hints.md`.

**Forbidden (this pass):** Per Atlas rule — no full `Chk/Ln.md`, no full test modules, no complete capstone implementation.

---

## Maestro note

After Atlas finishes, use **Maestro** with **`@python/data-structures/course/progress.yaml`** and **`@python/data-structures/course/spine.yaml`** for Riley/Marsh handoffs.
