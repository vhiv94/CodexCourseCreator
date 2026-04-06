# Overview

This reference course is the canonical minimal example for the current lesson-first workflow. It stays deliberately small, uses plain `python3`, and keeps the planning artifacts inside a normal course root even though that root lives under `course/reference-module/`.

## Intake and shape

The intake assumption for this example is simple:

- the learner already recognizes basic Python syntax
- they still need practice turning messy text input into small, reliable helper functions
- one chapter is enough, so modules would be unnecessary overhead

That is why this spine uses a chapter-only shape with three narrow lessons.

## Project arc

The learner builds a tiny study-session summary script in `main.py`.

- `Ch1/L1` cleans the learner name.
- `Ch1/L2` filters raw practice notes into a stable list.
- `Ch1/L3` composes both helpers into one deterministic summary string and prints it from `main()`.

The project stays small on purpose so the workflow itself is easy to inspect.

## Assessment flow

This example makes the default two-assessment pattern visible before lesson generation:

1. `course/PRESTRUCTURE_ASSESSMENT.md` captures scope and pacing before the spine shape is locked.
2. `course/Ch1/ASSESSMENT.md` captures Chapter 1 readiness before lesson authoring begins.

`course/progress.yaml` is intentionally parked on the Chapter 1 prechapter assessment so routing behavior is explicit:

- `recent_assessment.kind: prestructure`
- `current_target.type: assessment`
- `current_target.ref: prechapter:Ch1`

After that assessment, routing should hand off to lesson authoring for `Ch1/L1` first.

## Lesson-first contract

Each lesson row in `course/spine.yaml` includes an explicit `assignment` block. That assignment is the primary contract for learner work.

- `L1` and `L2` are artifact/demo first and have no test metadata.
- `L3` includes optional supporting test metadata because the final output is easy to check mechanically.

This keeps the example aligned to the current repo contract: lesson scope first, tests second when they materially help.

## Commands

Run the script:

```bash
python3 main.py
```

Optional final-lesson test check when `pytest` is available:

```bash
python3 -m pytest main_test.py -m lesson_ch1_l3
```
