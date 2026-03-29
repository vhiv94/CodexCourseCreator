# End-to-end Maestro, Riley, Marsh flow (worked example)

This walkthrough uses `python/reference-module/` and demonstrates one full lesson handoff loop.

## 1) Start state

`course/progress.yaml`:

```yaml
last_completed: null
next_target: Ch1/L1
```

`course/spine.yaml` maps `Ch1/L1` to:

- `test_glob: main_test.py`
- `lesson_selector: lesson_ch1_l1`

## 2) Maestro run (orchestrator)

User message to Maestro:

```text
done none yet, start this course
```

Expected Maestro output shape:

1. Progress patch
2. Riley block
3. Marsh block

Example:

```yaml
# progress patch
last_completed: null
next_target: Ch1/L1
```

```text
[RILEY BLOCK]
Attach rule: kwon-test-architect
Context:
- @python/reference-module/course/progress.yaml
- @python/reference-module/course/spine.yaml
- @python/reference-module/course/overview.md
Task:
- Append tests for Ch1/L1 in @python/reference-module/main_test.py
- Use marker @pytest.mark.lesson_ch1_l1
- Do not modify unrelated lesson blocks.
```

```text
[MARSH BLOCK]
Attach rule: marsh-lesson-author
Context:
- @python/reference-module/course/progress.yaml
- @python/reference-module/course/spine.yaml
- @python/reference-module/course/overview.md
- @course/templates/lesson.md
Task:
- Author @python/reference-module/Ch1/L1.md for Ch1/L1 only.
- Keep acceptance criteria test-mappable to selector lesson_ch1_l1.
```

## 3) Riley output behavior

Riley appends a new `Ch1/L1` block to the end of `main_test.py` with marker `lesson_ch1_l1`.

The file remains append-only: old lesson blocks are not rewritten when later lessons are added.

## 4) Marsh output behavior

Marsh writes `Ch1/L1.md` aligned with the same lesson selector contract and test expectations.

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

Then Maestro emits the next Riley/Marsh pair for `Ch1/L2` with selector `lesson_ch1_l2`. Riley appends new tests to `main_test.py` and Marsh writes `Ch1/L2.md`.
