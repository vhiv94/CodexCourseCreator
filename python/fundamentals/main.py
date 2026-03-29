"""Learner entrypoint for Python fundamentals (fresh reset)."""


def format_banner(app_label: str) -> str:
    clean_label = app_label.strip()
    return f"=== {clean_label} ==="


def normalize_note(raw_note: str) -> str:
    return raw_note.strip()


def is_valid_note(note: str) -> bool:
    return bool(note)


def append_note(notes: list[str], raw_note: str) -> list[str]:
    cleaned = normalize_note(raw_note)
    if not is_valid_note(cleaned):
        raise ValueError("note must not be empty")
    return [*notes, cleaned]


def render_log_view(notes: list[str], app_label: str = "Study Log") -> str:
    lines = [format_banner(app_label)]
    if not notes:
        lines.append("(no notes yet)")
    else:
        for idx, note in enumerate(notes, start=1):
            lines.append(f"{idx}. {note}")
    return "\n".join(lines)


def summarize_progress(notes: list[str]) -> dict[str, int]:
    total_characters = sum(len(note) for note in notes)
    return {"total_notes": len(notes), "total_characters": total_characters}


def main() -> None:
    print(format_banner("Study Log"))


if __name__ == "__main__":
    main()
