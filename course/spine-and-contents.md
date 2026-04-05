# Spine (`course/spine.yaml`) and `CONTENTS.md`

The **spine** is the machine-facing planning document. **`CONTENTS.md`** is the human-facing table of contents. They must describe the same ordering and titles.

The schema now supports two valid course shapes:

- short or moderate courses with top-level `chapters`
- longer courses with `modules -> chapters -> lessons`

## File locations

| Artifact | Path |
|----------|------|
| Spine | `course/spine.yaml` or `course/spine.json` |
| Schema | `course/spine.schema.json` |
| Example | `course/spine.example.yaml` |
| Human TOC | `CONTENTS.md` at the course root |

## Planning metadata

`delivery` is optional metadata that helps Atlas and Maestro coordinate adaptive generation.

Supported fields:

- `generation_mode`: `full_spine`, `module_batch`, `chapter_batch`, or `adaptive`
- `default_batch_size`: typical number of chapters or lessons to generate at once
- `assessment_checkpoints`: whether reassessment is expected beyond intake

## Course shape

### Chapter-only courses

Use top-level `chapters:` when the course is short enough that modules would be unnecessary overhead.

### Module-aware courses

Use `modules:` only when the course has **three or more** meaningful module groupings.

- Each module uses `id` such as `M1`, `M2`, `M3`
- Each module has a `title`, `summary`, and nested `chapters`
- Chapter `dir` values remain `Ch1`, `Ch2`, and so on
- Lesson refs and dependencies still use `Ch#/L#`

## On-disk lesson layout (`Ch#/L#`)

For each chapter `dir` and lesson `id`:

| Role | Path pattern |
|------|--------------|
| Lesson prose | `{dir}/{id}.md` |
| Hint prose | `{dir}/{id}-hint.md` when `hints: true` |
| Tests | resolved by `test_glob` |

Modules organize planning and the human table of contents. They do not introduce a separate on-disk `M#/` folder layer.

## Lesson metadata

Each lesson keeps the existing core fields and may now include:

- `kind`: `lesson`, `review`, `quiz`, or `assessment`
- `assessment_goal`: required when `kind` is `quiz` or `assessment`

This lets the spine represent lightweight reviews and checkpoints without pretending every row is a normal build step.

## Test contract

- Legacy per-lesson test files such as `Ch1/L1.py` remain migration-compatible.
- Canonical Python flow uses append-only `main_test.py` or split files like `main_test_ch2.py`.
- When `test_glob` points at a `main_test*.py` file, `lesson_selector` is required.
- `lesson_selector` uses the pytest marker form `lesson_ch<chapter>_l<lesson>`.

## `depends_on`

- `depends_on` is a list of `Ch#/L#` refs.
- First lessons may use `depends_on: []`.
- Dependencies describe conceptual and generation order even when content is authored in batches.

## `CONTENTS.md` format

### Chapter-only format

Use a level-3 heading per chapter:

```markdown
### Ch1: Foundations

1. First lesson
2. Second lesson
```

### Module-aware format

Use a level-2 heading per module, then level-3 headings for chapters:

```markdown
## M1: Foundations

### Ch1: Request Response Basics

1. Map the HTTP cycle
2. Quick review of status code families
```

Rules:

1. Module headings, when present, must be exactly `## {id}: {title}`.
2. Chapter headings must be exactly `### {dir}: {title}`.
3. Numbered lesson lines must match lesson titles in order within that chapter.
4. Numbering resets at each chapter.
5. Do not list filenames in `CONTENTS.md`.

## Validation

- Update `course/spine.*` and `CONTENTS.md` together.
- Run `python3 scripts/validate_repo.py` from the repository root after edits.
- Expect current validators to support both legacy chapter-only and module-aware course shapes during the migration period.

## Optional JSON spine

If you use `course/spine.json`, keep the same property names and nesting as the schema; only the serialization format changes.
