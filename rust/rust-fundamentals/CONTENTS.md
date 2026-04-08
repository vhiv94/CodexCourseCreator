# Contents

## M1: Foundations and Tooling

### Ch1: First Contact with Cargo

1. Create and run the Log Summary crate
2. Read the crate layout and `main`
3. Print structured output with `println!`
4. Capture one line of user input
5. Checkpoint on first Cargo and CLI input steps

### Ch2: Variables, Functions, and Control Flow

1. Prechapter check on variables, functions, and control flow
2. Bind values with `let` and `mut`
3. Write helper functions that return values
4. Choose behavior with `if` and `match`
5. Repeat work with loops
6. Checkpoint on variables, helpers, and control flow

## M2: Text and Collections

### Ch3: Strings and Text Boundaries

1. Compare `String` and `&str`
2. Build and update log text
3. Split one input line into fields
4. Review chars, bytes, and UTF-8 boundaries

### Ch4: Collections for In-Memory State

1. Store log records in a `Vec`
2. Use tuples and arrays for small fixed shapes
3. Summarize levels with a `HashMap`
4. Checkpoint on text and collection choices

## M3: Modeling Log Data

### Ch5: Structs for Log Records

1. Replace a tuple with `struct LogEntry`
2. Add associated constructors for common inputs
3. Derive debug output for domain structs
4. Separate parsing from stored data
5. Checkpoint on struct-based log modeling

### Ch6: Enums and Pattern Matching

1. Model log levels with an enum
2. Encode parse outcomes with another enum
3. Use `Option` and `Result` for parser decisions
4. Render summaries with `match`
5. Checkpoint on enum-driven parser decisions

## M4: Organizing Real Programs

### Ch7: Modules, Crates, and Project Layout

1. Split parser and model code into modules
2. Expose a small crate-level API
3. Use `use` imports to keep code readable
4. Keep `main` thin and explicit
5. Checkpoint on crate organization and `main` flow

### Ch8: File Persistence and Basic Tooling

1. Read log lines from a text file
2. Write a summary report back to disk
3. Add a first `cargo test` smoke check
4. Use `cargo fmt` and `cargo clippy`
5. Checkpoint on persistence and Rust tooling habits

## M5: Ownership and Borrowing

### Ch9: Ownership and Moves

1. Trace ownership through scope boundaries
2. Watch moves happen across function calls
3. Return ownership or clone on purpose
4. Reduce unnecessary clones in helpers
5. Checkpoint on ownership and move choices

### Ch10: References, Borrowing, and Slices

1. Borrow shared data with `&`
2. Mutate safely with `&mut`
3. Accept `&str` and slices in parser APIs
4. Practical ownership checkpoint

## M6: Reuse and Extension

### Ch11: Traits and Generics in Small Doses

1. Define a trait for project summaries
2. Use one generic helper over borrowed input
3. Choose trait bounds over copy-pasted code
4. Review abstraction choices

### Ch12: Project Integration and Tooling Handoff

1. Refactor around stable domain modules
2. Add subcommands for summary and filter workflows
3. Export data in a report-friendly shape
4. Capstone review and next-course handoff
