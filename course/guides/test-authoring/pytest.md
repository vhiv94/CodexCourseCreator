# pytest — selector-scoped test appendix

Use when the course repo runs **[pytest](https://docs.pytest.org/)** on Python. Goal: **one lesson → one selector in append-only `main_test.py` → one scoped invocation** (e.g. **`uv run pytest main_test.py -m lesson_ch2_l3`** when using [uv](https://github.com/astral-sh/uv)), aligned with spine `test_glob` + `lesson_selector`.

In this monorepo, **Python** courses live under **`python/<course-slug>/`**; run **`uv sync`** / **`uv run pytest …`** from **that** directory (see **`python/README.md`** at repo root).

## File layout

- **Lesson tests**: append tests into module-root `main_test.py` and mark each lesson block with its spine `lesson_selector` (for example `@pytest.mark.lesson_ch1_l1`).
- **Spine contract**: set `test_glob: main_test.py` and one unique `lesson_selector` per lesson.
- **Learner implementation**: packages under `src/` (import as `from mycourse import ...`) or flat modules per `overview.md`; tests import from the **learner-facing** package layout only.

## Discovery and configuration

- Root **`pyproject.toml`** or **`pytest.ini`**: set sensible defaults (`testpaths` if you use a conventional tree; `pythonpath = ["src"]` when applicable).
- Keep marker names deterministic and unique; avoid free-form `-k` expressions for lesson routing when markers are available.

## Dependencies ([uv](https://docs.astral.sh/uv/) projects)

When the course uses **uv** (recommended in this workspace), treat packaging like a real app project:

- **Install what the repo already declares:** `uv sync` from the course root (uses `pyproject.toml` + lockfile).
- **Add a library** (replaces `pip install …` in tutorials): `uv add requests` (updates `pyproject.toml` and the lockfile).
- **Dev-only tools:** `uv add --dev ruff` (or your chosen stack).
- **Teaching note:** if external material says `pip install pytest`, the local equivalent is `uv add pytest` (often already in `dependencies`).

Do not tell learners to maintain a hand-written **`requirements.txt`** alongside `pyproject.toml` unless the course explicitly uses that layout.

## Lesson-local runner (canonical one-liner)

With **uv** (recommended for Python courses in this workspace), run **only** one lesson selector from the course root:

```bash
uv run pytest main_test.py -m lesson_ch1_l1
```

Use **`uv run pytest main_test.py -m <lesson_selector>`** in `overview.md`, every `Ch#/L#.md`, and footer comments in `main_test.py`. If a repo does not use uv, document one alternative there (for example `python -m pytest main_test.py -m lesson_ch1_l1` after activating its venv).

## `conftest.py` scope

- **Root `conftest.py`**: shared fixtures for many chapters—keep fixtures **generic**; lesson-specific fixture coupling belongs in `Chk/conftest.py` or in the lesson file under a `pytest_plugins` pattern only when documented.
- Do not rely on **collection order** across files; each lesson file should stand alone.

## Shared fixtures / helpers

- Prefer **`tests/support/`** or **`Chk/_support/`** for reusable factories; import them from the lesson test module.
- Spine **`test_glob`** should be `main_test.py`, while **`lesson_selector`** scopes to one lesson.

## Spine and naming

- **`test_glob`**: use `main_test.py`.
- **`lesson_selector`**: use `lesson_ch<chapter>_l<lesson>` (for example `lesson_ch2_l3`) and apply it as a pytest marker on that lesson's tests.
- **`depends_on`**: import learner APIs established in earlier lessons; avoid re-asserting every detail of prior lessons unless this lesson extends a contract.

## Pitfalls

- **Implicit namespace packages / imports**: document how learners resolve imports in `overview.md`—prefer `pythonpath` in pytest config and a project installed with **`uv sync`**; avoid **`pip install`** in prose when the repo is uv-managed (**`uv add`** / **`uv sync`** instead).
- **`__init__.py` in `Ch*`**: usually omit so `Ch1` is not accidentally treated as a regular package you import; if you add packages under `Chk`, document clearly.
- **Parametrization explosion**: parametrized tests are fine when they clarify the concept; avoid combinatorial tables that obscure the lesson goal.

## Riley checklist (pytest-specific)

Riley’s deliverable is append-only updates to **`main_test.py`**; running **`uv run pytest`** afterward is optional and usually done by Maestro, CI, or the learner—not a requirement for Riley to execute locally.

- [ ] Spine row uses `test_glob: main_test.py` and a unique `lesson_selector`.
- [ ] `main_test.py` has the lesson's pytest marker on all tests for that lesson.
- [ ] `uv run pytest main_test.py -m <lesson_selector>` would collect **only** tests intended for that lesson (no accidental extra tests)—design for that scope even if you don’t run the command.
- [ ] Deterministic: no network, no wall-clock dependence unless the lesson requires it (then use controlled fixtures).
