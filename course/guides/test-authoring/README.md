# Test authoring appendices (non-agent docs)

These files are **reference patterns** for wiring per-lesson tests in this course layout (append-only `main_test.py` with lesson selectors; lesson prose stays in `Ch#/L#.md`). They are **not** Cursor rules. For agent behavior and guardrails, use **Riley Kwon** (`.cursor/rules/kwon-test-architect.mdc`).

When scaffolding a new course repo, pick **one** primary stack, copy the relevant patterns into `course/overview.md` (runner commands, fixture dirs), and keep each lesson’s spine selector contract (`test_glob` + `lesson_selector`) scoped to **that lesson only**.

**Python in this workspace:** Each course lives under **`python/<slug>/`** (see **[`python/README.md`](../../python/README.md)**). Use **[uv](https://docs.astral.sh/uv/)** — **`uv sync`**, **`uv add`** (not `pip install`), **`uv run pytest main_test.py -m <lesson_selector>`** (see [pytest.md](pytest.md)).

| Ecosystem | Document |
|-----------|----------|
| Vitest (TypeScript / Vite, ESM) | [vitest.md](vitest.md) |
| pytest (Python) | [pytest.md](pytest.md) |
| Jest (TypeScript / JavaScript) | [jest.md](jest.md) |

Add new appendices here as needed (for example Deno, Go `testing`, Rust `cargo test`) using the same section outline as the existing guides.
