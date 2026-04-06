"""Canonical minimal reference script for the lesson-first workflow."""


def normalize_name(raw_name: str) -> str:
    """Return one cleaned learner name for display."""
    clean_name = raw_name.strip()
    return clean_name or "Learner"


def collect_notes(raw_notes: list[str]) -> list[str]:
    """Keep only cleaned, non-empty practice notes."""
    cleaned_notes: list[str] = []
    for raw_note in raw_notes:
        clean_note = raw_note.strip()
        if clean_note:
            cleaned_notes.append(clean_note)
    return cleaned_notes


def build_progress_summary(raw_name: str, raw_notes: list[str]) -> str:
    """Compose the cleaned name and notes into one summary string."""
    name = normalize_name(raw_name)
    notes = collect_notes(raw_notes)

    lines = [f"Study summary for {name}"]
    if notes:
        lines.extend(f"- {note}" for note in notes)
    else:
        lines.append("- No practice notes yet.")
    return "\n".join(lines)


def main() -> None:
    sample_summary = build_progress_summary(
        "  Ada  ",
        [" reviewed lists ", " ", "wrote a helper function  "],
    )
    print(sample_summary)


if __name__ == "__main__":
    main()
