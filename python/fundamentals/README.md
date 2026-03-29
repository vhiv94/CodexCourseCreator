# Python fundamentals (course reset)

Beginner Python course rooted here. Spine: `course/spine.yaml`. Track progress: `course/progress.yaml`.
This fresh reset currently covers two chapters with six lessons, all using selector-scoped tests in `main_test.py`.

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
uv run pytest main_test.py -m lesson_ch1_l1
```

Swap the selector for other lessons per `course/spine.yaml` (`lesson_selector`). Learner entrypoint for this reset is module-root `main.py`. More context: [`course/overview.md`](course/overview.md).
