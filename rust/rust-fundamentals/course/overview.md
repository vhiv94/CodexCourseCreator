# Overview

`rust/rust-fundamentals/` is a new module-aware Rust course for a learner who has some typed-language and low-level background, but wants Rust taught gently from scratch rather than assumed.

## Planning assumptions

- Rust itself is new territory, so the course should not skip syntax or tooling orientation.
- The pace should stay slow and deliberate, especially before ownership and borrowing.
- The learner wants a broad foundation first rather than immediate specialization.
- The project should feel practical, CLI-first, and rich enough to support later Rust tooling, data-processing, or backend study.

## Project arc

The course centers on a **Log Summary CLI**:

- a small command-line tool for reading log files, parsing lines, and printing grouped summaries
- starts with `cargo`, `main`, terminal I/O, strings, and control flow
- grows into structs, enums, collections, file persistence, modules, and tests
- later becomes the vehicle for ownership, borrowing, slices, traits, and light generics
- ends with reusable summary output that could feed a later Rust tooling or data-processing project

This project was chosen because it matches the Rust book's early CLI emphasis, makes file and text handling central, and gives Rust-specific concepts a concrete home without forcing networking, async work, or heavy framework setup too early.

## Module rationale

- `M1` establishes the Rust toolchain and the first executable wins.
- `M2` builds fluency with text and collections, which the project needs before richer modeling.
- `M3` introduces typed log modeling with structs, enums, `Option`, `Result`, and `match`.
- `M4` turns the single-file prototype into a more realistic crate with persistence and baseline tooling.
- `M5` isolates ownership and borrowing as the course's main Rust-specific hurdle, but keeps the practice grounded in common project code.
- `M6` adds just enough traits and generics to support reuse and a clean handoff to later Rust study.

## Delivery strategy

- `generation_mode: lesson_first`
- short-answer pre-structure assessment already captured during planning
- short-answer prechapter assessments expected before writing each chapter's lesson batch
- default next step: run the Chapter 1 prechapter assessment, then generate one narrow lesson at a time

## Topics intentionally included in course one

- Rust tooling and crate structure
- strings and collections
- structs and enums
- pattern matching
- modules and crates
- practical `Option` / `Result` use
- ownership, borrowing, and slices
- traits and generics in small doses

## Topics intentionally deferred

- async Rust
- real web frameworks
- concurrency primitives
- explicit lifetimes as a major design topic
- advanced macro authoring

Those topics fit better in a follow-up Rust backend, tooling, or intermediate Rust course once the learner trusts the core language model.
