# Glossary — Python fundamentals

Short definitions for readers new to programming. Titles in **bold** match terms used in lessons and chatter around Python.

## Environment and tools

**Python** — A programming language and the ecosystem around it. In this course, “Python” usually means **Python 3**.

**uv** — A fast **Python project and package manager**. You **`uv sync`** to install everything listed in **`pyproject.toml`**, **`uv add some-package`** to add a dependency (the usual replacement for **`pip install some-package`** in beginner material), and **`uv run …`** to run a command in the project environment (for example tests). Install uv once per machine from the official docs.

**Interpreter** — The program that reads your `.py` source and runs it. When you type `python3 your_file.py`, you are asking the interpreter to execute that file.

**REPL** — “Read–eval–print loop”: an interactive Python session (typing `python3` with no file) where each line is read, evaluated, and the result printed. Useful for quick experiments; the course project is primarily **scripts** you run as files.

**Terminal / shell** — A text window where you run commands (`python3`, `uv run pytest`, `cd`, etc.). The **current working directory** matters for paths like `notes.txt`.

**IDE / editor** — Where you write code (VS Code, Cursor, etc.). Not the same as the terminal, though they often sit side by side.

## Programs and files

**Script** — A `.py` file meant to be **run** start-to-finish (e.g. your study log program).

**Module** — Usually a `.py` file treated as a unit of useful code; in bigger projects, modules are **imported** from other code.

**Package** — A folder of modules (often with `__init__.py` in classic layouts). This course may place learner code under `src/` as a small package layout—see `overview.md`.

**Comment** — Text in source code ignored by Python, starting with `#` (or using triple-quoted strings only when meant as docstrings—Marsh will clarify usage in lessons).

## Code building blocks

**Variable** — A name that refers to a value. You **assign** with `=` (e.g. `title = "Study log"`).

**Value / data** — What actually sits in memory: numbers, text, lists, etc.

**String** — Text in quotes (`"hello"`, `'hi'`). You can **concatenate** strings with `+`.

**Function** — A named chunk of code you **call** with parentheses. It can take **arguments** and optionally **return** a result to the caller.

**Parameter** — A name listed in a `def` line; it receives the **argument** the caller passes in.

**Return value** — What a function sends back with `return`; the caller can store or use it.

**Scope** — Which parts of the code can see which names. “Inside the function” vs “at the top level” behaves differently—in **`Split Prompting from Formatting`** you focus on keeping that tidy.

**Conditional** — `if`, optional `elif`, and `else`: choose which lines run based on a **boolean** (true/false) condition.

**Loop** — Repeating code: **`while`** repeats while a condition holds; **`for`** walks over each item in a sequence (e.g. a list).

**List** — An ordered collection: `[a, b, c]`. Often used with `for` and `.append(...)`.

**Dictionary (`dict`)** — A collection of **key → value** pairs, like a labeled tray of settings (`{"filename": "log.txt", ...}`).

## Files and robustness

**Path** — A string or `Path` object describing **where** a file lives on disk (relative or absolute).

**Open / read / write / append** — File operations: read existing text, overwrite, or **appendnew lines at the end**. Appending is typical for logs.

**Context manager** — The `with open(...) as f:` pattern so files close reliably even when errors occur.

**Exception** — A runtime error Python raises (e.g. file missing, bad conversion). **`try` / `except`** lets you **handle** predictable problems without crashing the whole program.

## Testing

**pytest** — A test runner (here invoked via **`uv run pytest`** so the project environment stays correct). **Test functions** are usually named `test_*`. Running `uv run pytest Ch2/L3.py` should execute only that lesson’s tests if Riley scoped the file correctly.

**Fixture** — Helper setup (temporary folder, fake input) used by tests; may live in `conftest.py` or `tests/support/` per `overview.md`.

## CLI terms

**Command-line argument** — Text after the program name when you run it (`python3 study_log.py list`). Often read from **`sys.argv`** or a small **argparse** layer.

If a term is still fuzzy, skim the matching lesson’s **`concept`** in `spine.yaml`—that line is the single idea the lesson centers on.
