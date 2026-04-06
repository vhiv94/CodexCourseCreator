# End-to-end workflow example

This walkthrough is kept as a legacy handoff example for `python/reference-module/`.

For the current canonical minimal workflow, use `course/reference-module/WORKFLOW_EXAMPLE.md`.

## 1) Start state

`course/progress.yaml`:

```yaml
last_completed: null
next_target: Ch1/L1
```

`course/spine.yaml` maps `Ch1/L1` to:

- `assignment.summary: Build format_greeting(name) for the learner entrypoint.`
- `test_glob: main_test.py`
- `lesson_selector: lesson_ch1_l1`

## 2) Next-step routing pass

User message:

```text
done none yet, start this course
```

Expected output shape:

1. Progress patch
2. Lesson authoring block
3. Optional test authoring block

Example:

```yaml
# progress patch
last_completed: null
next_target: Ch1/L1
```

```text
[LESSON AUTHORING BLOCK]
Attach rule: lesson-authoring
Context:
- @python/reference-module/course/progress.yaml
- @python/reference-module/course/spine.yaml
- @python/reference-module/course/overview.md
- @course/templates/lesson.md
Task:
- Author @python/reference-module/Ch1/L1.md for Ch1/L1 only.
- Keep the assignment contract narrow and learner-facing.
```

```text
[OPTIONAL TEST AUTHORING BLOCK]
Attach rule: test-authoring
Context:
- @python/reference-module/course/progress.yaml
- @python/reference-module/course/spine.yaml
- @python/reference-module/course/overview.md
- @python/reference-module/Ch1/L1.md
Task:
- Append tests for Ch1/L1 in @python/reference-module/main_test.py
- Use marker @pytest.mark.lesson_ch1_l1
- Do not modify unrelated lesson blocks.
```

## 3) Lesson authoring behavior

Lesson authoring writes `Ch1/L1.md` from the lesson assignment contract first.

## 4) Optional test authoring behavior

If the lesson includes test metadata, test authoring then appends a new `Ch1/L1` block to the end of `main_test.py` with marker `lesson_ch1_l1`.

The file remains append-only: old lesson blocks are not rewritten when later lessons are added.

## 5) Learner loop

Learner implements `main.py` until:

```bash
uv run pytest main_test.py -m lesson_ch1_l1
```

passes.

## 6) Advance progress and repeat

After finishing L1, update progress:

```yaml
last_completed: Ch1/L1
next_target: Ch1/L2
```

Then next-step routing emits the next lesson-authoring block for `Ch1/L2`, plus a test-authoring follow-up only when `Ch1/L2` includes test metadata. Test authoring appends new tests to `main_test.py` and lesson authoring writes `Ch1/L2.md`.
