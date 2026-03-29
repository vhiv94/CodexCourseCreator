# Hints: Ln — short hint-sheet title

Use this file **only** when `course/spine.*` has **`hints: true`** for this lesson. Path pattern: `{chapter-dir}/{lesson-id}.hints.md` (e.g. `Ch1/L3.hints.md`).

These notes are **optional reading** when stuck. They may include sketches, “consider…”, and small pseudocode. They must **not** be a complete copy-paste solution that satisfies every test without thought.

## Allowed hint depth (rubric)

Use the shallowest level that unblocks the learner.

- **Level 1 - Direction only (default):** explain invariant/goal and where to look in tests.
- **Level 2 - Strategy sketch:** give 3-6 high-level steps or partial pseudocode without final naming/details.
- **Level 3 - Focused edge-case nudge:** call out one tricky case to check (empty input, tie-break, ordering).
- **Not allowed:** full function/class implementations, exact final return expressions for every case, or end-to-end code that can be pasted to pass all tests directly.

## When to open this file

*(One sentence: what “stuck” looks like for this lesson—without giving the answer.)*

## Orientation

*(Remind the learner what invariant or interface the tests care about; point back to the test file path.)*

**Tests:** *(from spine `test_glob` + `lesson_selector`, e.g. `main_test.py` + `lesson_ch1_l3`)*

## Nudges

*(Numbered or short sections—each a strategic nudge, not a full derivation.)*

1. **Nudge title** — *(direction, edge case, or representation choice to consider)*
2. **Nudge title** — *(…)*

Example nudge quality:

- **Good:** "Process docs in original corpus order so output lengths align with ids."
- **Bad:** "Paste this complete loop and return tuple..." (full answer).

## Algorithm or structure sketch (optional)

*(For harder modules only: high-level steps, loop idea, or pseudocode. Partial—learners must connect this to their code and the tests.)*

```text
# pseudocode / bullet sketch only — not a full solution

```

Keep sketches abstract (data flow and invariants), not final code.

## Pitfalls to double-check

- *(common bug or wrong assumption—still not the full fix)*
- *(…)*
