# Reference Module

This is the primary worked example for the current Course Creator workflow.

- Canonical path: `course/reference-module/`
- Stack: plain `python3`, stdlib-first
- Flow: pre-structure assessment -> spine/progress -> prechapter assessment -> lesson authoring first -> optional tests second

The tiny project arc builds a study-session summary script in three narrow lessons:

1. normalize the learner name
2. keep only real practice notes
3. render one deterministic text summary

Key files:

- `CONTENTS.md`
- `course/spine.yaml`
- `course/progress.yaml`
- `course/PRESTRUCTURE_ASSESSMENT.md`
- `course/Ch1/ASSESSMENT.md`
- `course/Ch1/L1.md` to `course/Ch1/L3.md`
- `main.py`
- optional `main_test.py`
- `WORKFLOW_EXAMPLE.md`

Run the script with:

```bash
python3 main.py
```

If you want the optional lesson-scoped test check for the final lesson and `pytest` is available:

```bash
python3 -m pytest main_test.py -m lesson_ch1_l3
```

The older `python/reference-module/` tree is kept only as a legacy archive of the earlier selector-scoped `uv` example.
