# Python fundamentals (course)

Beginner Python course rooted here. Spine: `course/spine.yaml`. Track progress: `course/progress.yaml`.

This folder is a **[uv](https://docs.astral.sh/uv/)** project: dependencies live in **`pyproject.toml`** (and the lockfile). Use **uv**, not **`pip install`**, when adding packages.

**First-time / after pulling changes:** from this directory, install everything the course declares:

```bash
uv sync
```

**Add a library** (writes `pyproject.toml` + updates the lockfile—same role as `pip install` in older tutorials):

```bash
uv add httpx
```

**Dev-only tools** (e.g. a formatter): `uv add --dev ruff`. **Remove:** `uv remove <package>`.

**Tests:** run a single lesson from this directory (uv uses `pyproject.toml` / `.venv` automatically):

```bash
uv run pytest Ch1/L1.py
```

Swap `Chk/Ln.py` for other lessons per the spine’s `test_glob`. More context: [`course/overview.md`](course/overview.md).
