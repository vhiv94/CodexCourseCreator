# Lesson title

Use the exact lesson title from `CONTENTS.md` / `course/spine.*`. Do not include `Ch#/L#` in the heading.

Write one concept-first narrative block (no `## Concept` subheader). This block should integrate:

- definition and mechanics of the lesson concept
- key tools and why each matters in this lesson
- why this lesson matters in the project arc
- learning objectives phrased in learner-facing language
- boundary/tradeoff clarifications and common misconceptions

Optional: include at most one short fenced micro-example in this narrative block. It must be illustrative only and not paste-ready for tests.

## Assigned task(s)

Describe what to build or change in learner-owned code, with outcomes and constraints (no line-by-line recipe). Integrate acceptance criteria directly in this section.

Suggested shape:

- **Build/Change:** *(what learner implements)*
- **Expected outcomes / acceptance criteria:**
  - [ ] *(behavior or contract the tests assert)*
  - [ ] *(behavior or contract the tests assert)*
  - [ ] *(add rows until the checklist covers test intent)*
- **Evidence (tests):** `test_glob` + `lesson_selector` from spine (for example `main_test.py` + `lesson_ch1_l1`)

## Further reading (optional)

Keep short. Include only references that directly support this lesson.

---

If the spine marks this lesson with **`hints: true`**, optional algorithmic nudges and sketches live only in **`Ln-hint.md`** next to this file—not in this lesson body.
