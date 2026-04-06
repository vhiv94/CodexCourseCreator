# Rust Fundamentals - Build a Request Journal CLI

This course root plans a gentle first Rust course for a learner who is comfortable with typed languages and some low-level ideas, but has not yet explored Rust itself in this project.

## Course shape

- module-aware course structure
- slow, lesson-first pacing
- short-answer assessments before structure and before each chapter batch
- a dedicated late module for ownership and borrowing

## Project

The course project is a **Request Journal CLI**:

- starts as a small terminal tool for recording route ideas, request notes, and response summaries
- teaches Rust fundamentals through `cargo`, terminal I/O, strings, collections, structs, enums, modules, and file persistence
- prepares a clean handoff into a later Rust backend or services course without forcing networking too early

## Files in this course root

- `CONTENTS.md` mirrors the planned module, chapter, and lesson order.
- `course/overview.md` explains the learning arc and course rationale.
- `course/spine.yaml` defines the planning contract for modules, chapters, and lessons.
- `course/progress.yaml` stores the current routing state.
- `RUST_BOOK_EARLY_NOTES.md` condenses the opening Rust book chapters and the planning conclusions taken from them.

## Current status

This root currently contains planning artifacts only. Lessons, assessments, learner implementation files, and tests have not been generated yet.

## Validation

From the repository root:

```bash
python3 scripts/validate_repo.py
```
