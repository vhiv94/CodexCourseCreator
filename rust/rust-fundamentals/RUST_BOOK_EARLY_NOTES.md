# Rust Book Early Notes

These notes condense the opening arc of the official Rust book and translate it into planning guidance for this course.

## Chapters Reviewed

- `ch01` Getting Started
- `ch02` Programming a Guessing Game
- `ch03` Common Programming Concepts
- `ch04` Understanding Ownership

## What The Book Front-Loads

- Rust starts with tooling immediately: `rustup`, `cargo`, project creation, build, and run.
- The first meaningful project is a tiny CLI, not a pure syntax tour.
- `String`, `stdin`, formatting, `match`, and crates show up very early inside real code.
- Rust delays the full ownership explanation until after basic syntax and control flow are familiar.
- Ownership, borrowing, and slices are presented as the first truly Rust-shaped mental model.

## Teaching Implications

- The course should begin with executable wins, not compiler theory.
- `cargo` deserves first-class treatment because it is part of the everyday Rust experience.
- A small CLI with text input/output is the best introductory project shape.
- Early lessons should normalize reading compiler messages instead of hiding them.
- Ownership should be its own late module after learners already trust the language basics.
- The ownership module should stay practical: moves, borrowing, mutable versus immutable access, and slices in common cases before any deeper lifetime material.

## Concepts Worth Teaching Before Ownership

- `fn`, `let`, `mut`, expressions, and control flow
- formatting with `println!`
- `String` creation and updates
- `match` for branching
- bringing standard-library items into scope with `use`
- project structure through `cargo new`

## Ownership Notes To Preserve

- Moving owned values is a normal default, not a special edge case.
- References exist to let code inspect or mutate data without taking ownership.
- Rust allows either many immutable references or one mutable reference at a time.
- Slices solve real API design problems and should be taught as ergonomics, not trivia.
- The borrow checker is easier to teach when learners can compare a bad API shape to a good one.

## Course Design Decisions Supported By These Notes

- Use `modules -> chapters -> lessons`.
- Keep pacing gentle and lesson steps narrow.
- Start with a CLI-first project that grows toward service-style thinking later.
- Delay the dedicated ownership and borrowing module until after data modeling and program organization.
- Include explicit review/checkpoint moments before the ownership module.

## Best-Fit Intro Project

Recommended primary project:

- **Request Journal CLI**
- A small command-line tool that records route ideas, sample requests, and response notes for a future tiny service.
- Starts with prints, input, and text parsing.
- Grows into structs, enums, file persistence, modules, and later borrow-checker-friendly helper APIs.

Why it fits:

- It is concrete without requiring real networking too early.
- It naturally uses `String`, `&str`, collections, pattern matching, and file I/O.
- It leaves a clean path into a future Rust backend or web-services course.

## Other Good Intro Project Options

- **Log Summary CLI**: read a text file, parse lines, and print grouped summaries.
- **File-Backed Task Tracker**: build a simple CRUD-style terminal app around tasks or notes.
- **Route Sketcher**: design endpoints, methods, and status responses without implementing a server yet.

## What To Avoid In Course One

- Async networking too early
- Heavy macro authoring
- Explicit lifetime-heavy API design as a central theme
- A capstone that depends on too much ecosystem setup before the learner understands the language core
