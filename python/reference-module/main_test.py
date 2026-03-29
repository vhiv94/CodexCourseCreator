"""Append-only lesson tests for the reference module."""

from __future__ import annotations

import pytest

from main import append_note, format_greeting


# ============================
# BEGIN LESSON BLOCK: Ch1/L1
# selector: lesson_ch1_l1
# ============================
@pytest.mark.lesson_ch1_l1
def test_format_greeting_trims_and_formats_name() -> None:
    assert format_greeting("  Ada  ") == "Hello, Ada!"


@pytest.mark.lesson_ch1_l1
def test_format_greeting_keeps_simple_name() -> None:
    assert format_greeting("Sam") == "Hello, Sam!"


# ============================
# BEGIN LESSON BLOCK: Ch1/L2
# selector: lesson_ch1_l2
# Appended later; do not rewrite prior blocks.
# ============================
@pytest.mark.lesson_ch1_l2
def test_append_note_adds_clean_note_to_end() -> None:
    assert append_note(["first"], " second  ") == ["first", "second"]


@pytest.mark.lesson_ch1_l2
def test_append_note_rejects_empty_after_strip() -> None:
    with pytest.raises(ValueError):
        append_note(["first"], "   ")
