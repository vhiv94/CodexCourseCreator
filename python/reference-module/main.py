"""Reference learner entrypoint for main_test.py selector flow."""


def format_greeting(name: str) -> str:
    """Return a trimmed greeting line."""
    clean_name = name.strip()
    return f"Hello, {clean_name}!"


def append_note(notes: list[str], raw_note: str) -> list[str]:
    """Append a non-empty stripped note and return a new list."""
    clean_note = raw_note.strip()
    if not clean_note:
        raise ValueError("note must not be empty")
    return [*notes, clean_note]


def main() -> None:
    print(format_greeting("Learner"))


if __name__ == "__main__":
    main()
