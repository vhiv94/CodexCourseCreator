# Spine (`course/spine.yaml`) and `CONTENTS.md`

The **spine** is machine- and agent-facing structured data. **`CONTENTS.md`** (project root) is the human table of contents. They describe the **same** chapter and lesson order and **must stay in sync**.

## File locations

| Artifact | Path |
|----------|------|
| Spine | `course/spine.yaml` (or `course/spine.json` — same fields) |
| Schema | `course/spine.schema.json` (JSON Schema for YAML/JSON spine files) |
| Example | `course/spine.example.yaml` |
| Human TOC | **`CONTENTS.md` at repository root** (not under `course/`) |

## On-disk lesson layout (`Ch#/L#`)

For each chapter `dir` (e.g. `Ch1`) and lesson `id` (e.g. `L1`):

| Role | Path pattern |
|------|----------------|
| Lesson prose | `{dir}/{id}.md` — e.g. `Ch1/L1.md` |
| This lesson’s tests | Resolved by **`test_glob`** — typically `{dir}/{id}.<ext>` (e.g. `Ch1/L1.py`, `Ch2/L3.test.ts`) |
| Hints (optional) | `{dir}/{id}.hints.md` — **required** when spine `hints: true` |

**`test_glob`** must resolve **only** that lesson’s test entrypoint (plus any paths you deliberately include, such as shared fixtures — document those in `course/overview.md`). Convention: one primary test file per lesson; globs stay narrow so `uv run pytest Ch1/L1.py` / `vitest run Ch2/L1.test.ts` style commands stay lesson-local.

## `depends_on`

- List of **`Ch#/L#`** strings: chapter `dir`, `/`, lesson `id` (e.g. `Ch1/L1`, `Ch2/L3`).
- **First lesson(s)** in the course may use `depends_on: []`.
- Defines prerequisite lessons for Maestro ordering and author handoffs; it does not replace whatever your test runner uses.

## `CONTENTS.md` format (project root)

Rules (match the agent plan):

1. For each chapter, a **level-3 heading**: exactly `### {dir}: {title}`  
   - Example: `### Ch1: Foundations`  
   - `{dir}` and `{title}` must match `chapters[].dir` and `chapters[].title` in the spine **character for character**.

2. Under that heading, **numbered lesson titles only** — `1. `, `2. `, … — in global lesson order **within that chapter**. Numbering **resets** at each new chapter.

3. Lines must match **`lessons[].title`** in spine order (first line `1.` ↔ first lesson in `chapters[i].lessons`, etc.).

4. Do **not** list filenames in `CONTENTS.md`; names follow `Chk/Ln` stems as above.

### Example spine chapter

```yaml
chapters:
  - dir: Ch1
    title: Foundations
    lessons:
      - id: L1
        title: "Environment and first green test"
        # ...
      - id: L2
        title: "Core behavior from examples"
```

### Matching `CONTENTS.md` excerpt

```markdown
### Ch1: Foundations

1. Environment and first green test
2. Core behavior from examples
```

## Validation

- Spine files should validate against **`course/spine.schema.json`** (e.g. `ajv-cli`, IDE YAML schema mapping, or a small CI check).
- When editing, update **both** `course/spine.yaml` and root **`CONTENTS.md`** in the same change so titles and order cannot drift.

## Optional: JSON spine

If you use **`course/spine.json`** instead of YAML, keep the same property names and nesting as in the schema; only the serialization format changes.
