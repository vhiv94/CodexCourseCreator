# Python Fundamentals — overview

## What you are building

One **command-line study log**: you run a Python program, add short timestamped notes about what you studied, list what is saved, and keep everything in a **plain text file** so your log survives closing the terminal. By the end of the course, the program behaves like a tiny real utility—not a one-off demo script.

## Why this shape

Absolute beginners learn faster when every new idea **lands in the same program**. Strings, variables, `if`, loops, functions, lists, files, and a minimal “how to run it” interface each move the log one step closer to something you might actually use.

## Behavioral end-state

When you finish the last lesson, a learner’s project should **approximately**:

- Run from the terminal with different **modes** (for example: add entries vs. show the log), using **command-line arguments**—not by editing the source between runs.
- **Load** existing log lines from disk at startup when the file exists, and **append** new lines so data persists across sessions.
- Keep **configuration** (names, filenames, quit phrase, labels) in a small, understandable structure instead of scattered magic strings.
- **Fail gracefully** when something goes wrong reading or interpreting stored data, without crashing silently or losing the whole log.

Exact filenames, flag names, and internal function names are left for Marsh’s lessons and Riley’s tests to pin down; the spine’s `project_step` fields describe the **capability**, not a single prescribed API.

## Prerequisites

- Comfortable using a computer: files, folders, opening a terminal, and running commands someone gives you.
- **No** prior programming experience assumed.

Environment: a working **Python 3** install you can run as `python` or `python3` from a terminal. Install instructions vary by OS; your lessons or local README can link to official docs.

For **this** course repo, learners and authors also need **[uv](https://docs.astral.sh/uv/getting-started/installation/)** (install once per machine). From **`python/fundamentals/`**, run **`uv sync`** so `pyproject.toml` and the lockfile create/update **`.venv`** and install **pytest** and any other declared dependencies—do not instruct **`pip install -r requirements.txt`** here; treat **`uv add`** (with the package name) as the way to add a dependency, and **`uv remove`** to drop one.

## How chapters map to the arc

| Chapter | Role in the study log |
|--------|------------------------|
| **Ch1 — Your First Python Program** | Run Python; print output; shape text with strings; comment the script so the “study log” direction is clear. |
| **Ch2 — Talking to the User** | Remember strings in variables; read input; validate with `if`; repeat prompts with `while` until the user quits. |
| **Ch3 — Organizing with Functions** | Replace a growing tangle of inline code with small functions: formatting, timestamps, prompting vs. building lines. |
| **Ch4 — Lists and Loops** | Hold many log lines in memory; display them with `for`; append as the user types so state matches behavior. |
| **Ch5 — Saving to Disk** | Append to a file; load on startup; represent paths sensibly; wire load + save so the tool is usable day to day. |
| **Ch6 — Finishing Touches** | Narrow `try` / `except`; centralize settings in a **dict**; expose **modes** via `sys.argv` (or a thin argparse layer), completing the CLI shape. |

## Test stack (pytest)

This course uses **pytest** with **one lesson → one test module** under the course root `python/fundamentals/`. Dependencies (including pytest) are managed with **[uv](https://github.com/astral-sh/uv)** via this folder’s `pyproject.toml` and lockfile.

- **Install / update the environment:** from `python/fundamentals/`, run **`uv sync`** (creates or updates **`.venv`** from the lockfile). To **add** a new dependency, use **`uv add some-package`**—not **`pip install`**. **`uv remove some-package`** drops it from the project.
- **Layout (planned for Riley):** test functions live in `Chk/Ln.py` (e.g. `Ch1/L1.py`). Each file should collect **only** the tests for that lesson.
- **How to run one lesson:** from `python/fundamentals/`, use uv so the project venv and pytest stay in sync:

  ```bash
  uv run pytest Ch1/L1.py
  ```

  Same pattern for any `Chk/Ln.py` in the spine’s `test_glob`. **Document and use `uv run pytest`** in lessons, README, and CI so runners do not depend on manually activating a venv.

- **Learner implementation:** will live under `src/` (or another layout Marsh documents). Use **root** `pyproject.toml` or `pytest.ini` with `pythonpath = ["src"]` (or equivalent) so tests import the learner package without manual `PYTHONPATH` hacks. If you add **shared fixtures** (for temporary log directories, fake stdin, etc.), place them in a documented support area (for example `tests/support/` under this course) and import from the lesson test module—keep each lesson’s `test_glob` pointing at **that lesson’s file only**.

See the repo-wide appendix [course/guides/test-authoring/pytest.md](../../course/guides/test-authoring/pytest.md) for `conftest` scope, pitfalls, and Riley’s checklist.

## Shared fixtures (expectation)

Riley may introduce **temporary directories or files** for safe file I/O tests and **stdin/stdout helpers** for “user types this” scenarios. If so, those helpers live outside individual `Chk/Ln.py` files but are documented here: **`tests/support/`** under `python/fundamentals/` (create when implementing tests). Spine `test_glob` values remain the single **lesson** module path.

## What this document is not

Not a line-by-line coding recipe. Marsh’s lessons carry steps and explanations; Riley’s tests express contracts. Use the spine’s `concept` and `project_step` fields as the bridge between “what to learn” and “what the program gains next.”
