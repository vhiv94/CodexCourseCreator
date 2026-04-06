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

`delivery` is optional metadata that helps planning and next-step routing coordinate adaptive generation.

Supported fields:

- `generation_mode`: `lesson_first`, `full_spine`, `module_batch`, `chapter_batch`, or `adaptive`
- `default_batch_size`: typical number of chapters or lessons to generate at once
- `assessment_checkpoints`: whether reassessment is expected beyond intake
- `assessment_format`: default assessment style such as `short_answer`
- `prestructure_assessment`: whether planning starts with a short-answer assessment before deciding chapters vs modules
- `prechapter_assessments`: whether each chapter should begin with a short-answer assessment before lesson generation

## Course shape

### Chapter-only courses

Use top-level `chapters:` when the course is short enough that modules would be unnecessary overhead.

### Module-aware courses

Use `modules:` only when the course has **three or more** meaningful module groupings.

- Each module uses `id` such as `M1`, `M2`, `M3`
- Each module has a `title`, `summary`, and nested `chapters`
- Chapter `dir` values remain `Ch1`, `Ch2`, and so on
- Lesson refs and dependencies still use `Ch#/L#`

## On-disk lesson layout

Logical lesson refs still use chapter + lesson ids such as `Ch1/L3`, but the prose path depends on the course shape.

### Chapter-only courses

For each chapter `dir` and lesson `id`:

| Role | Path pattern |
|------|--------------|
| Lesson prose | `course/{dir}/{id}.md` |
| Hint prose | `course/{dir}/{id}-hint.md` when `hints: true` |
| Tests | optional, resolved by `test_glob` when present |

### Module-aware courses

For each module `id`, chapter `dir`, and lesson `id`:

| Role | Path pattern |
|------|--------------|
| Lesson prose | `course/{module-id}/{dir}/{id}.md` |
| Hint prose | `course/{module-id}/{dir}/{id}-hint.md` when `hints: true` |
| Tests | optional, resolved by `test_glob` when present |

Modules therefore affect both planning and on-disk lesson placement, while lesson refs, dependencies, and selectors remain stable as `Ch#/L#`.

## Lesson metadata

Each lesson keeps the existing core fields and may now include:

- `kind`: `lesson`, `review`, `quiz`, or `assessment`
- `assignment.summary`: the concrete learner task for the lesson
- `assignment.outcomes`: optional learner-visible acceptance points for lesson authoring
- `assignment.evidence`: optional notes about what counts as proof of completion
- `assessment_goal`: required when `kind` is `quiz` or `assessment`

This lets the spine represent lightweight reviews, checkpoints, and explicit assignment contracts without pretending every row is a normal build step.

## Optional test contract

- `test_glob` is optional. Lessons may be assignment-first with no test metadata.
- Legacy per-lesson test files such as `Ch1/L1.py` remain migration-compatible.
- Canonical Python flow uses append-only `main_test.py` or split files like `main_test_ch2.py` when the course chooses to ship tests.
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
