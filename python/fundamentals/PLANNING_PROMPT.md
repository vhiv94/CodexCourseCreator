# Planning prompt — Python fundamentals (copy-paste)

**Enable rule:** `planning` (attach that Cursor rule in Composer or chat before running).

**Workspace layout:** New **Python** courses belong under **`python/<course-slug>/`** with **[uv](https://docs.astral.sh/uv/)**; the planning pass may **`uv init`** (e.g. **`uv init --no-readme`**) when `pyproject.toml` is missing, then **`uv add pytest`**. This prompt targets **`fundamentals`** only. See **[`python/README.md`](../README.md)** for the shared convention.

**Workflow caveat:** Default routing often assumes `course/spine.*` at the workspace root. This course lives under `python/fundamentals/`. After planning finishes, either open `python/fundamentals` as its own workspace (with rules/schemas available there) or keep this repo as root and in workflow chats always cite `@python/fundamentals/course/spine.yaml` and `@python/fundamentals/course/progress.yaml` so prompts target the right spine and progress.

---

Paste everything below the line into the agent with the planning rule enabled.

---

**Objective:** Design a **full** beginner Python course. Start by running a short-answer pre-structure assessment before deciding the final course shape. Write **only** the planning artifacts, not full lesson markdown, not full test code, and not learner implementation in `src/`.

**Output paths (all relative to repo root `coursecreator`):**

- `python/fundamentals/course/spine.yaml` — must validate against `@course/spine.schema.json`
- `python/fundamentals/CONTENTS.md` — human outline; chapter headings `### Chk: <Chapter title>` and per-chapter numbered lesson titles must match the spine **verbatim** (order and spelling)
- `python/fundamentals/course/overview.md` — motivation, behavioral end-state, prerequisites, how chapters map to the arc; test stack **pytest** (patterns in `@course/guides/test-authoring/pytest.md`); not a step-by-step coding walkthrough
- Optional: `python/fundamentals/course/glossary.md` — helpful for absolute beginners (interpreter, REPL, variable, function, string, etc.)

**User topic and audience (in their words):**

- Topic: *“Learn the basics with Python.”*
- Audience: *Absolute beginner—no prior programming experience* (comfort using a computer and files/terminal is enough to state as the only prerequisite).
- Pedagogy: One **cohesive capstone-style arc**. Pick one small but real project that grows chapter by chapter. Keep **one concise concept per lesson**, let each lesson advance **one** project step, include an explicit lesson `assignment`, ensure **`depends_on`** forms a sensible DAG, and use `hints: true` only where struggling beginners are likely. Add `test_glob` plus `lesson_selector` only for lessons that should ship tests.

**Do not** ask planning to write per-lesson tests or lesson prose in this pass unless you explicitly expand scope later. Test authoring and lesson authoring handle those after the spine exists.

**Assessment convention:** keep `delivery.assessment_format: short_answer`, `prestructure_assessment: true`, and `prechapter_assessments: true`. Before any future chapter lesson batch is written, expect a short-answer `ASSESSMENT.md` step for that chapter.

---

## After `uv init` / clone (learner / agent note)

This course folder uses **[uv](https://docs.astral.sh/uv/)** for Python and **pytest**.

- **Install dependencies:** from `python/fundamentals/`, run **`uv sync`**.
- **Add a library** when the curriculum needs it: **`uv add package-name`**.
- **Verify a lesson:** **`uv run pytest main_test.py -m <lesson_selector>`**

Do not document bare **`pytest …`** or raw **`pip install …`** for this course. Use **`uv run pytest`** and **`uv add`** when tests exist. See `course/overview.md` and `README.md` in this folder.
