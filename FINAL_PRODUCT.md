# Final Product Vision

This file describes the long-term website direction for Course Creator. It is intentionally separate from the current Cursor-era workflow docs.

## Product thesis

The eventual product is a website that creates courses tailored to each learner from a single prompt plus follow-up questions.

The differentiator is personalization:

- course scope is unique to the learner,
- the sequence can adapt over time,
- reusable templates may exist behind the scenes, but the delivered course should feel custom.

## Expected user flow

1. The learner describes what they want to learn.
2. The system asks the minimum set of questions needed to narrow or expand the topic.
3. The system runs a light knowledge assessment.
4. The system generates a personalized course plan.
5. The learner works through the course in a viewer that resumes from the last completed step.
6. The system can reassess and regenerate future content when needed.

## Product surfaces

### Course creator

- Accepts the initial learner prompt.
- Collects scope-defining answers.
- Runs the initial assessment.
- Produces a personalized course.

### Course list

- Shows the learner's generated courses.
- Reflects that courses are user-specific rather than globally identical.

### Course manager

- Lets the learner revise, extend, or regenerate a course.
- Supports re-scoping or changing direction without starting from scratch.

### Course viewer

- Resumes where the learner left off.
- Uses a dual-pane layout: lesson on the left, editor/work area on the right.
- Includes navigation for previous lesson, next lesson, chapter selection, and lesson selection.

## Community and support

- A future version may include a community space where learners help each other.
- Reusable course templates or backend planning structures may support generation efficiency.

## Delivery economics

- The final product likely should not generate content one lesson at a time by default because that would be expensive.
- Chapter-sized generation or similarly batched generation is a more realistic default.
- Those batches may include lessons, review quizzes, and the information needed to choose the next batch.

## Relationship to this repo

- This repository is the system-design and contract layer for the current implementation phase.
- The website should eventually inherit the same scoping, assessment, planning, and validation ideas, but not necessarily the same Cursor-specific rule mechanics.
