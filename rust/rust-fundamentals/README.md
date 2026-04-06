# Rust Fundamentals - Build a Log Summary CLI

This course root plans a gentle first Rust course for a learner who is comfortable with typed languages and some low-level ideas, but has not yet explored Rust itself in this project.

## Course shape

- module-aware course structure
- slow, lesson-first pacing
- short-answer assessments before structure and before each chapter batch
- a dedicated late module for ownership and borrowing

## Project

The course project is a **Log Summary CLI**:

- starts as a small terminal tool for reading log lines, parsing them, and printing grouped summaries
- teaches Rust fundamentals through `cargo`, terminal I/O, strings, collections, structs, enums, modules, and file persistence
- prepares a clean handoff into a later Rust tooling, data-processing, or backend course without forcing networking too early

## Files in this course root

- `CONTENTS.md` mirrors the planned module, chapter, and lesson order.
- `course/overview.md` explains the learning arc and course rationale.
- `course/spine.yaml` defines the planning contract for modules, chapters, and lessons.
- `course/progress.yaml` stores the current routing state.
- `RUST_BOOK_EARLY_NOTES.md` condenses the opening Rust book chapters and the planning conclusions taken from them.

## Current status

Planning artifacts, `course/progress.yaml`, and lesson prose live under `course/` (for example `course/M1/Ch1/L1.md`). Learner-owned crate sources and per-lesson tests are still created by you alongside those lessons.

## Validation

From the repository root:

```bash
python3 scripts/validate_repo.py
```
