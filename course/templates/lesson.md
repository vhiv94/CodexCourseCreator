# Ln: Lesson title

Replace the heading with the spine lesson `id` (e.g. `L1`) and the **exact** lesson title from `CONTENTS.md` / `course/spine.*` (must match character for character).

## Concept

*(2–5 short paragraphs: the one idea this lesson teaches—definitions, mental model, boundaries. **Optional:** at most one short fenced code example here, very basic illustration only—not step-by-step implementation, not the assigned task or anything paste-ready for tests. Omit if prose is enough.)*

**Good vs bad (Concept):**

- **Good:** "A queue is FIFO: first item in is first item out. In this lesson, that invariant prevents starvation while merging work items."
- **Bad:** "Write `merge_streams` by creating a list, sorting every loop, then returning tuples exactly like this..." (implementation recipe).

## Why it matters in this project

*(How this concept connects to `project_step` and the larger arc in `course/overview.md`.)*

## Learning objectives

By the end of this lesson, you will be able to:

- [ ] *(objective tied to evidence the tests can show)*
- [ ] *(objective tied to evidence the tests can show)*
- [ ] *(optional third objective)*

## Assigned task(s)

*(What to build or change in learner-owned code, e.g. under `src/`. Describe outcomes and constraints; do **not** give a line-by-line recipe or full algorithm walkthrough. When the spine sets `hints: true`, keep strategy high-level here and defer sketches to `Ln.hints.md`.)*

**Good vs bad (Assigned task(s)):**

- **Good:** "Add a function that returns the top `k` scores with deterministic tie-breaking by `doc_id`."
- **Bad:** "Copy this heap loop, then call `heappush` in this exact order..." (too prescriptive).

## Acceptance criteria

Treat **public tests** as the specification. Check each item when your implementation satisfies it.

- [ ] *(behavior or contract the tests assert—plain language)*
- [ ] *(behavior or contract the tests assert)*
- [ ] *(add rows until the checklist covers the lesson’s test intent)*

**Evidence (tests):** *(from spine: `test_glob` + `lesson_selector`, e.g. `main_test.py` + `lesson_ch1_l1`)*

Criteria should be concrete, externally observable, and map to test assertions.

**Good vs bad (Acceptance criteria):**

- **Good:** "Given an empty corpus, `summarize_corpus` returns `(0, [], 0)`."
- **Good:** "If two docs share score, lower `doc_id` appears first."
- **Bad:** "Use a dictionary internally." (implementation detail, not behavior).
- **Bad:** "Code looks clean and efficient." (not testable).

## How you’ll know you’re done

Run the **lesson-local** command for this file (document the exact command in `course/overview.md` or here). Tests for this lesson only should pass.

```text
uv run pytest main_test.py -m lesson_ch1_l1
```

*(Replace with the real lesson-local command for your stack—for Python + uv courses, use `uv run pytest main_test.py -m <lesson_selector>`.)*

## Common misconceptions

- **Misconception** — *(why it’s wrong; what to check in the tests instead)*
- **Misconception** — *(brief correction)*

## Further reading (optional)

*(Links or `reads[]` from the spine; keep optional and short.)*

---

If the spine marks this lesson with **`hints: true`**, optional algorithmic nudges and sketches live only in **`Ln.hints.md`** next to this file—not in this lesson body.
