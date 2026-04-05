# Course Scope

This file defines the educational design rules for the current Course Creator system.

## Scope calibration

Every new course starts by calibrating scope before generating a full spine.

- If the learner request is too broad, ask narrowing questions.
- If the learner request is too narrow, ask expansion questions.
- Run a light knowledge assessment early.
- Use the assessment to decide where the course needs depth, where it needs review, and how aggressively it can move.
- Do not assume prior knowledge means a topic should be skipped entirely.

## Hierarchy

The canonical planning hierarchy is:

- `modules -> chapters -> lessons` for long courses.
- `chapters -> lessons` for shorter courses where modules would add unnecessary structure.

## Modules

Modules are optional and should be used only when they add real structure.

- A module is a broad slice of the subject, almost like a course within a course.
- Modules are appropriate when the course has several clearly different conceptual domains.
- If the planned course would only have one or two modules, omit modules and use chapters directly.
- Courses may have as many modules as needed when the scope justifies them.

Examples:

- A short language-fundamentals course may not need modules.
- A backend fundamentals course may use modules for requests, databases, servers, deployment, and data flow.
- A "learn a new language" course may use modules for fundamentals, objects, networking, and tooling.

## Chapters

Chapters should represent a narrow concept cluster.

- A chapter should feel like one leaf concept area, not a vague bucket.
- Chapters can be short or long, but they should stay conceptually coherent.
- A long module may contain 10 or more chapters, with roughly 6 as a healthy average.
- A long course can have many chapters even when modules are omitted.

Examples:

- In fundamentals: variables, functions, lists, sets, dictionaries.
- In a requests module: response codes, GET, POST, request validation.
- In an OOP module: class layout, object instantiation, inheritance.

## Lessons

Lessons should be as narrow as possible while still advancing the project.

- Each lesson should teach one concrete step of execution, reasoning, or review.
- Lessons build on one another rather than trying to dump an entire concept at once.
- Quiz or review lessons are allowed, but should be used intentionally.
- A long chapter may contain 15 or more lessons, with roughly 8 as a healthy average.

Examples:

- In a variables chapter: basic types, declaration, assignment.
- In a response-code chapter: status families, common codes, choosing the right status.
- In an objects chapter: what an object is, instantiate an object, pass an object to a function.

## Assessments

Assessment is part of the system, not an afterthought.

- The course-creation phase should include a very light initial knowledge assessment.
- The goal is not to gatekeep or skip everything the learner knows.
- The goal is to set scope, pacing, and review depth.
- Additional quizzes may appear inside lessons, at chapter endings, or before generating the next batch.
- For adaptive flows, a chapter-end or pre-batch assessment can help decide what should come next.

## Adaptive generation

The system does not have to generate the full course up front every time.

- Some courses may benefit from a detailed initial spine.
- Some courses may be better generated chapter by chapter.
- The right generation mode should be chosen during scoping.
- Short, stable subjects may use a fuller up-front spine.
- Open-ended or learner-sensitive subjects may use lighter planning plus reassessment between batches.

## Project philosophy

- Prefer a coherent project arc over disconnected exercises.
- The project can still be small or "toy" in scale; the key is continuity and motivation.
- A course may eventually support more than one project, but a single coherent arc is the current default.

## Current repository implications

- Rules should support scoping, assessment, planning, chapter batching, and reassessment.
- Schemas should support both module-aware and chapter-only courses.
- Validation should preserve backward compatibility where practical and document the migration path where not.
- The repo should treat `AGENTS.md`, `SCOPE.md`, and `FINAL_PRODUCT.md` as stable system docs rather than hiding process inside role prompts.
