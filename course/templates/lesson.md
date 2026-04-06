# Lesson title

Use the exact lesson title from `CONTENTS.md` / `course/spine.*`. Do not include `Ch#/L#` in the heading.

Write one concept-first narrative block (no `## Concept` subheader). This block should integrate:

- definition and mechanics of the lesson concept
- key tools and why each matters in this lesson
- why this lesson matters in the project arc
- learning objectives phrased in learner-facing language
- boundary/tradeoff clarifications and common misconceptions

Optional: include at most one short fenced micro-example in this narrative block. It must be illustrative only and not paste-ready for the full assignment.

## Assigned task(s)

Describe what to build, change, explain, or review in learner-owned work, with outcomes and constraints (no line-by-line recipe). Integrate acceptance criteria directly in this section.

Suggested shape:

- **Build/Change:** *(what learner implements)*
- **Expected outcomes / acceptance criteria:**
  - [ ] *(learner-visible outcome from `assignment.outcomes` or the lesson contract)*
  - [ ] *(another concrete acceptance point)*
  - [ ] *(add rows until the checklist covers the lesson scope)*
- **Evidence:** describe the artifact, explanation, demo, or review the learner should produce.
- **Optional test evidence:** include `test_glob` + `lesson_selector` only when the spine supplies them (for example `main_test.py` + `lesson_ch1_l1`)

## Further reading (optional)

Keep short. Include only references that directly support this lesson.

---

If the spine marks this lesson with **`hints: true`**, optional algorithmic nudges and sketches live only in the sibling hint file next to the lesson body:

- chapter-only courses: **`course/Ch#/Ln-hint.md`**
- module-aware courses: **`course/M#/Ch#/Ln-hint.md`**

Do not put those nudges in this lesson body.
