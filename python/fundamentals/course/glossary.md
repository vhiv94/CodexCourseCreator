# Glossary — Python Fundamentals Personal Tracker

## Core language ideas

**Variable** — A named reference to a value, created with assignment (`=`).

**Value** — Actual data (text, numbers, booleans, collections, objects).

**Type** — A category of value (for example `str`, `int`, `float`, `bool`) that controls what operations are valid.

**String (`str`)** — Text data in quotes. Strings are immutable and iterable.

**Integer (`int`)** — Whole number values like `0`, `7`, or `-13`.

**Float (`float`)** — Decimal number values like `3.14` or `0.5`.

**Boolean (`bool`)** — `True` or `False`, typically produced by comparisons.

**Operator** — Symbol or keyword that combines values (`+`, `-`, `*`, `/`, `==`, `and`, `or`, `not`).

## Python conventions

**PEP 8** — Python style guidance; emphasizes readability and consistent naming.

**Pythonic** — Idiomatic Python style that is clear and readable for other Python developers.

**snake_case** — Lowercase words joined by underscores; standard for variables and function names in Python.

**Main guard** — `if __name__ == "__main__":` block that runs code only when a file is executed directly.

## Control flow and data structures

**Conditional** — `if/elif/else` branching based on boolean conditions.

**Loop** — Repetition using `for` or `while`.

**Iterable** — Any object you can loop over one value at a time (`str`, `list`, `tuple`, `set`, many others).

**List** — Ordered, mutable collection.

**Tuple** — Ordered, immutable collection.

**Dictionary (`dict`)** — Key-value mapping for named lookup.

**Set** — Unordered collection of unique values.

## Functions and modules

**Function** — Reusable block of code defined with `def`.

**Parameter** — Variable name inside a function signature.

**Argument** — Actual value passed to a function call.

**Return value** — Value produced by `return` and sent back to the caller.

**Scope** — Region where a name is visible (local function scope vs module scope).

**Module** — Python file that contains code and can be imported.

**Import** — Statement that brings names from one module into another.

## Classes and objects

**Class** — Blueprint that defines data and behavior for objects.

**Object / instance** — Concrete value created from a class.

**Method** — Function defined inside a class.

**`__init__`** — Initializer method that sets up instance state during object creation.

**`__str__`** — User-facing string representation, used by `str(obj)` and `print(obj)`.

**`__repr__`** — Developer-facing representation, aimed at debugging clarity.

**Inheritance** — Child class reuses and extends behavior from a parent class.

**Polymorphism** — Same method name works across different classes with class-specific behavior.

## Files, errors, and tests

**File I/O** — Reading from and writing to files.

**Context manager** — `with ...:` pattern that manages setup/cleanup automatically.

**Exception** — Runtime error object raised when something goes wrong.

**try/except** — Structure for handling expected exceptions gracefully.

**pytest** — Test framework used in this module.

**Lesson selector** — Marker name such as `lesson_ch3_l2` used with `-m` to run one lesson's tests.

**uv** — Python project manager used for dependency installation and command execution (`uv sync`, `uv add`, `uv run pytest`).
