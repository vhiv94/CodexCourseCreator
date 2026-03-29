# Python Fundamentals - overview

## What you are building

You will build a command-line **Personal Tracker** from zero programming knowledge. The app starts as a small script, then grows into a modular program with functions, files, and classes that can add entries, list entries, and report summaries.

## Behavioral end-state

By the end of this module, the learner implementation should:

- Accept basic commands to add, list, and summarize tracker entries.
- Clean and validate text and numeric input before storing data.
- Represent tracker state using lists, tuples, dictionaries, and sets where each structure has a clear purpose.
- Sequence program behavior through a `main()` function and a final `if __name__ == "__main__":` call.
- Persist entries to disk and handle common runtime errors without crashing.
- Model entries with classes, including `__init__`, `__str__`, `__repr__`, and simple inheritance.

## Why this long-form redesign

This redesign intentionally uses many short lessons so beginners can learn one concept at a time while advancing a single coherent project. Each lesson maps to isolated tests in `main_test.py` using one marker selector.

## Prerequisites

- No prior programming experience.
- Ability to edit files and run terminal commands.
- Python 3 and [uv](https://docs.astral.sh/uv/getting-started/installation/) installed.

## Workflow and commands

From `python/fundamentals/`:

```bash
uv sync
uv run pytest main_test.py -m lesson_ch1_l1
```

To run a different lesson, swap the marker selector (for example, `lesson_ch4_l2`).

If you add third-party packages later in experiments, use:

```bash
uv add <package-name>
```

## Chapter arc

| Chapter | Learning focus |
|--------|-----------------|
| **Ch1 - First Contact with Python** | Running code, variables, data types, and operators. |
| **Ch2 - Strings and Flow of Text** | Strings as iterables, normalization, and branching logic. |
| **Ch3 - Collections for Tracker State** | Lists, tuples, dictionaries, sets, and state modeling. |
| **Ch4 - Reuse Logic with Functions** | Function interfaces, return values, scope, and composition. |
| **Ch5 - Program Organization and Main Flow** | Modules, imports, main guard, and sequential orchestration. |
| **Ch6 - Persistence and Error Handling** | File I/O, append workflows, exceptions, and data validation. |
| **Ch7 - Classes and Object Behavior** | Class structure, `__init__`, object methods, `__str__` and `__repr__`. |
| **Ch8 - Inheritance and Capstone Integration** | Base/child classes, polymorphism, and end-to-end integration. |

## Pythonic conventions emphasized

- Readable names over abbreviations.
- Small focused functions over monolithic scripts.
- Explicit branching and validation over hidden assumptions.
- Data structures chosen by intent (order, mutability, keyed lookup, uniqueness).

## Expansion questions for future module growth

These questions are included so you can extend this module later without redesigning from scratch:

1. Should user input eventually move from free text to `argparse` command flags?
2. Do you want lightweight static typing (`typing` hints) taught earlier or later?
3. Should persistence graduate from plain text files to JSON in this module or a follow-on module?
4. Do you want a dedicated chapter on debugging workflows (`pdb`, logging, tracebacks)?
5. Should testing grow from reading existing tests to writing learner-authored tests?
6. Do you want packaging/distribution basics (entry points, `pyproject.toml` metadata)?
7. Should inheritance remain shallow or include abstract base classes?
8. Should this course include an optional mini-project branch for students who finish early?

## Authoring note

Tests define behavior contracts in `main_test.py` and are scoped by lesson markers. Lesson prose is concept-first and avoids full copy-paste solutions so learners practice reasoning from evidence.
