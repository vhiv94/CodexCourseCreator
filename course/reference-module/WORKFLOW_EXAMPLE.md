# Workflow example

This walkthrough uses `course/reference-module/` as the canonical minimal lesson-first example.

## Start state

The course root already contains:

- a short-answer pre-structure assessment in `course/PRESTRUCTURE_ASSESSMENT.md`
- a chapter-only spine in `course/spine.yaml`
- a Chapter 1 prechapter assessment in `course/Ch1/ASSESSMENT.md`

`course/progress.yaml` intentionally shows that the pre-structure assessment has already informed the shape, while the prechapter assessment is still the active target:

```yaml
last_completed: null
next_target: Ch1/L1
current_target:
  type: assessment
  ref: prechapter:Ch1
generation_mode: lesson_first
recent_assessment:
  kind: prestructure
```

## Routing sequence

1. Run the pre-structure assessment before locking the course shape.
2. Decide that one chapter is enough for this tiny fundamentals project.
3. Run `course/Ch1/ASSESSMENT.md` before generating Chapter 1 lessons.
4. Route to lesson authoring for `course/Ch1/L1.md`.
5. Continue lesson by lesson unless the chapter is already well scoped for a bounded batch.
6. Add tests only after a lesson contract benefits from them.

## Lesson-first handoff

For `Ch1/L1`, lesson authoring should use:

- `course/reference-module/course/progress.yaml`
- `course/reference-module/course/spine.yaml`
- `course/reference-module/course/overview.md`
- `course/reference-module/course/Ch1/ASSESSMENT.md`
- `course/reference-module/course/Ch1/L1.md`

The assignment in the spine is the primary contract. No test block is needed for `L1` or `L2` because those lessons are artifact/demo first.

## Optional test follow-up

`Ch1/L3` is the first lesson that includes optional supporting test metadata:

- `test_glob: main_test.py`
- `lesson_selector: lesson_ch1_l3`

If `pytest` is available, the learner can run:

```bash
python3 -m pytest main_test.py -m lesson_ch1_l3
```

The test check is secondary to the lesson contract. The lesson still stands on its own as a learner-facing assignment.
