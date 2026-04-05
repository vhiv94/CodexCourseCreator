# Course Creator Agents

This repository is moving from a rigid "plan the whole chapter list first" workflow to a more adaptive course-design system.

The source-of-truth documents are:

- `AGENTS.md` for role boundaries and workflow.
- `SCOPE.md` for educational design rules.
- `FINAL_PRODUCT.md` for the long-term website vision.
- `course/spine.schema.json` and `course/progress.schema.json` for machine-enforced contracts.

## Core flow

1. Start with a learner prompt.
2. Narrow or expand the topic until the scope is teachable.
3. Run a light knowledge assessment to understand what needs depth versus review.
4. Decide the course shape:
   short courses may use `chapters -> lessons`,
   longer courses may use `modules -> chapters -> lessons`.
5. Produce or update a spine that reflects the chosen scope.
6. Generate content in batches, usually one chapter at a time.
7. Reassess progress before choosing the next batch.

## Role boundaries

### Atlas

Atlas is the planning role.

- Handles topic calibration, scope questions, and the initial knowledge check.
- Decides whether modules are needed.
- Produces or revises `course/spine.*`, `CONTENTS.md`, and `course/overview.md`.
- Keeps lesson scope narrow: one concrete step per lesson.
- Does not write full tests, full lesson bodies, or learner implementation code.

### Maestro

Maestro is the orchestrator.

- Reads `course/progress.*`, `course/spine.*`, and related docs.
- Decides whether the next action is scoping, assessment, replanning, chapter batching, or lesson authoring/testing.
- Routes work to Atlas, Riley, and Marsh.
- Updates adaptive progress metadata rather than assuming every course is a simple linear march through a fixed plan.
- Does not substitute for the specialist outputs unless explicitly asked.

### Riley

Riley is the test author.

- Writes behavior-first tests for the current batch.
- Keeps tests aligned to the spine contract and lesson scope.
- Preserves existing prior-lesson contracts.
- Prefers narrow, concrete lesson tests over broad end-to-end leaps.
- Does not write lesson prose or learner solutions.

### Marsh

Marsh is the lesson author.

- Writes lesson markdown and optional hint files for the current batch.
- Aligns the prose to the actual tests and current scope.
- Explains one focused step at a time.
- Supports review and quiz moments where the spine calls for them.
- Does not rewrite tests or redesign the course architecture.

## Routing guidance

- Use Atlas when the topic is new, too broad, too narrow, or the current spine no longer fits.
- Use Maestro when deciding what should happen next.
- Use Riley before Marsh for a new batch whenever tests are part of the contract.
- Use Marsh after Riley so lesson tasks and evidence match the real tests.

## Design principles

- Prefer coherent projects over disconnected toy exercises.
- Keep lessons small enough that each one teaches one executable step.
- Do not skip material entirely just because a learner is experienced; review still has value.
- Allow the course to adapt as more is learned about the student.
- Keep role instructions practical; names and personalities are optional, not essential.
