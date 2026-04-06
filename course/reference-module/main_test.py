"""Optional supporting tests for the reference module."""

from __future__ import annotations

import pytest

from main import build_progress_summary


@pytest.mark.lesson_ch1_l3
def test_build_progress_summary_uses_cleaned_name_and_notes() -> None:
    assert build_progress_summary(
        "  Ada  ",
        [" reviewed lists ", " wrote a helper function "],
    ) == "\n".join(
        [
            "Study summary for Ada",
            "- reviewed lists",
            "- wrote a helper function",
        ]
    )


@pytest.mark.lesson_ch1_l3
def test_build_progress_summary_handles_missing_notes() -> None:
    assert build_progress_summary("   ", [" ", "   "]) == "\n".join(
        [
            "Study summary for Learner",
            "- No practice notes yet.",
        ]
    )
