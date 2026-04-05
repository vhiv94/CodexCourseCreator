# Overview

This tiny module is a worked example of the canonical flow:

- Learner code lives in `main.py`.
- Riley appends tests in `main_test.py`.
- Each lesson is scoped with a unique marker selector from `course/spine.yaml`.
- Maestro routes progress updates and next-step handoffs.
- This example keeps its lesson prose in legacy `Ch#/L#.md` paths, but new courses should prefer `course/Ch#/L#.md`.

## Learning arc

- `Ch1/L1` introduces deterministic output with `format_greeting(name)`.
- `Ch1/L2` adds list updates plus validation with `append_note(notes, raw_note)`.

## Canonical test commands

From `python/reference-module/`:

```bash
uv run pytest main_test.py -m lesson_ch1_l1
uv run pytest main_test.py -m lesson_ch1_l2
uv run pytest main_test.py
```
