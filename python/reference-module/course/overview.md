# Overview

This tiny module is preserved as a legacy archive of the earlier selector-scoped Python flow.

For the current canonical minimal example, use `course/reference-module/` instead.

This archived module still demonstrates:

- learner code in `main.py`
- append-only tests in `main_test.py`
- lesson-specific selectors from `course/spine.yaml`
- a `uv`-managed pytest workflow

## Learning arc

- `Ch1/L1` introduces deterministic output with `format_greeting(name)`.
- `Ch1/L2` adds list updates plus validation with `append_note(notes, raw_note)`.

## Legacy test commands

From `python/reference-module/`:

```bash
uv run pytest main_test.py -m lesson_ch1_l1
uv run pytest main_test.py -m lesson_ch1_l2
uv run pytest main_test.py
```
