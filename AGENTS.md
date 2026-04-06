# Course Creator Workflow

This repository is moving from a rigid "plan the whole chapter list first" workflow to a more adaptive course-design system.

The source-of-truth documents are:

- `AGENTS.md` for workflow, responsibilities, and routing.
- `SCOPE.md` for educational design rules.
- `FINAL_PRODUCT.md` for the long-term website vision.
- `course/spine.schema.json` and `course/progress.schema.json` for machine-enforced contracts.

## Core flow

1. Start with a learner prompt.
2. Narrow or expand the topic until the scope is teachable.
3. Run a short-answer pre-structure assessment to understand what needs depth versus review before deciding the course shape.
4. Decide the course shape:
   short courses may use `chapters -> lessons`,
   longer courses may use `modules -> chapters -> lessons`.
5. Produce or update a spine that reflects the chosen scope.
6. Run a short-answer prechapter assessment before writing a chapter's lesson batch.
7. Generate lesson and assignment content in narrow increments, usually one lesson at a time unless a chapter is already well scoped.
8. Add tests after the lesson when they materially help the contract, feedback loop, or stack expectations.
9. Reassess progress before choosing the next increment or batch.

## Responsibility boundaries

### Planning

Planning turns a learner/topic request into a teachable course shape before lessons or tests are generated.

- Handles topic calibration, scope questions, and the pre-structure short-answer assessment.
- Decides whether modules are needed.
- Produces or revises `course/spine.*`, `CONTENTS.md`, and `course/overview.md`.
- Keeps lesson scope narrow: one concrete step per lesson.
- Does not write full lesson bodies, full tests, or learner implementation code.

### Next-step routing

Next-step routing decides what should happen now based on course state.

- Reads `AGENTS.md`, `SCOPE.md`, `course/progress.schema.json`, `course/spine.schema.json`, `.cursor/rules/shared-target-resolution.mdc`, and the current `course/progress.*`, `course/spine.*`, and `course/overview.md`.
- Treats `course/progress.*` as routing state rather than assuming a fixed linear sequence.
- Decides whether the next action is scope clarification, pre-structure assessment, spine planning or replanning, prechapter assessment, lesson or chapter batch generation, or reassessment/completion.
- Updates adaptive progress metadata rather than assuming every course is a simple linear march through a fixed plan.
- Routes work to planning, lesson authoring, or test authoring rather than silently substituting for those specialist outputs unless explicitly asked.

### Test authoring

Test authoring writes optional supporting tests for the current lesson or batch after the lesson contract is known.

- Keeps tests aligned to the spine contract, lesson assignment, and current scope.
- Preserves existing prior-lesson contracts and append-only test history.
- Prefers narrow, concrete lesson tests over broad end-to-end leaps.
- Uses the real `test_glob`, `lesson_selector`, `kind`, and `depends_on` values from the spine when the lesson includes test metadata.
- Does not write lesson prose or learner solutions.

### Lesson authoring

Lesson authoring writes lesson markdown and optional hint files for the current lesson or batch.

- Treats the lesson assignment as the primary contract for learner work and current scope.
- Explains one focused step at a time.
- Supports review and quiz moments where the spine calls for them.
- Defines learner-facing outcomes and evidence before any optional tests are added.
- Keeps lessons narrow and avoids solution leakage.
- Does not rewrite tests or redesign the course architecture.

## Next-step routing contract

### Read first

- `AGENTS.md`
- `SCOPE.md`
- `course/progress.schema.json`
- `course/spine.schema.json`
- `.cursor/rules/shared-target-resolution.mdc`
- current `course/progress.*`, `course/spine.*`, and `course/overview.md`

### Course states

Choose which state the course is currently in:

1. scope clarification
2. pre-structure assessment
3. spine planning or replanning
4. prechapter assessment
5. lesson or chapter batch generation
6. reassessment or completion

### Progress model

Treat `course/progress.*` as routing state.

Important fields:

- `last_completed`
- `next_target`
- `current_target`
- `generation_mode`
- `recent_assessment`
- `notes`

Use `current_target` for adaptive routing. Keep `next_target` for simple lesson-to-lesson compatibility.

### Routing rules

- If scope is unclear, ask scoping questions or route to planning.
- If learner level is unclear, ask a short-answer pre-structure assessment before deeper planning.
- Before generating a chapter's lessons for the first time, route through a short-answer prechapter assessment for that chapter.
- If `current_target.type` is `assessment` or `replan`, do not route to test authoring or lesson authoring yet.
- If `current_target.type` is `chapter` or `module`, emit a bounded batch for the incomplete lessons in that target.
- If no adaptive target is set, resolve lessons through `.cursor/rules/shared-target-resolution.mdc`.
- Prefer a single next lesson by default and use chapter-local batches only when the chapter is already well scoped.

## Routing guidance

- Use planning when the topic is new, too broad, too narrow, or the current spine no longer fits.
- Use next-step routing when deciding what should happen next from `course/progress.*` and `course/spine.*`.
- Use lesson authoring before test authoring for a new lesson or batch so the lesson assignment defines the contract first.
- Use test authoring after lesson authoring only when the course, stack, or lesson metadata says tests should exist.

## Design principles

- Prefer coherent projects over disconnected toy exercises.
- Keep lessons small enough that each one teaches one executable step.
- Do not skip material entirely just because a learner is experienced; review still has value.
- Allow the course to adapt as more is learned about the student.
- Keep role instructions practical; names and personalities are optional, not essential.
