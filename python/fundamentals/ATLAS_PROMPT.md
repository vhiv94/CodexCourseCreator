# Atlas prompt — Python fundamentals (copy-paste)

**Enable rule:** `atlas-learning-architect` (attach that Cursor rule in Composer or chat before running).

**Workspace layout:** New **Python** courses belong under **`python/<course-slug>/`** with **[uv](https://docs.astral.sh/uv/)**; **Atlas** may **`uv init`** (e.g. **`uv init --no-readme`**) when `pyproject.toml` is missing, then **`uv add pytest`**. This prompt targets **`fundamentals`** only—see **[`python/README.md`](../README.md)** for the shared convention.

**Maestro caveat:** Default Maestro assumes `course/spine.*` at the **workspace root**. This course lives under `python/fundamentals/`. After Atlas finishes, either open `python/fundamentals` as its own workspace (with rules/schemas available there—copy, symlink, or multi-root), **or** keep this repo as root and in Maestro/Riley/Marsh chats always cite `@python/fundamentals/course/spine.yaml` and `@python/fundamentals/course/progress.yaml` so prompts target the right spine and progress.

---

Paste everything below the line into the agent (with Atlas rule enabled).

---

**Objective:** Design a **full** beginner Python course. Write **only** the planning artifacts—**not** full lesson markdown, **not** full test code, **not** learner implementation in `src/`.

**Output paths (all relative to repo root `coursecreator`):**

- `python/fundamentals/course/spine.yaml` — must validate against `@course/spine.schema.json`
- `python/fundamentals/CONTENTS.md` — human outline; chapter headings `### Chk: <Chapter title>` and per-chapter numbered lesson titles must match the spine **verbatim** (order and spelling)
- `python/fundamentals/course/overview.md` — motivation, behavioral end-state, prerequisites, how chapters map to the arc; test stack **pytest** (patterns in `@course/guides/test-authoring/pytest.md`); not a step-by-step coding walkthrough
- Optional: `python/fundamentals/course/glossary.md` — helpful for absolute beginners (interpreter, REPL, variable, function, string, etc.)

**User topic and audience (in their words):**

- Topic: *“Learn the basics with Python.”*
- Audience: *Absolute beginner—no prior programming experience* (comfort using a computer and files/terminal is enough to state as the only prerequisite).
- Pedagogy: One **cohesive capstone-style arc**—pick one small but real project (e.g. CLI helper or text-based app) that grows chapter by chapter; **one concise concept per lesson**, each lesson advances **one** project step; canonical test contract is **`test_glob: main_test.py`** plus unique **`lesson_selector: lesson_ch<chapter>_l<lesson>`** so each lesson can run with marker scope; **`depends_on`** must form a sensible DAG. Use `hints: true` only where struggling beginners are likely; otherwise `hints: false`.

**Do not** ask Atlas to write per-lesson tests or lesson prose in this pass unless you explicitly expand scope later—Riley and Marsh handle those after the spine exists.

---

## After `uv init` / clone (learner / agent note)

This course folder uses **[uv](https://docs.astral.sh/uv/)** for Python and **pytest**.

- **Install dependencies:** from `python/fundamentals/`, run **`uv sync`** (not `pip install -r requirements.txt` unless the project intentionally uses that pattern—which this one does not).
- **Add a library** when the curriculum needs it: **`uv add package-name`** (equivalent role to `pip install package-name` in older material).
- **Verify a lesson:** **`uv run pytest main_test.py -m <lesson_selector>`**

Do not document bare **`pytest …`** or raw **`pip install …`** for this course—use **`uv run pytest`** and **`uv add`**. See `course/overview.md` and `README.md` in this folder.
