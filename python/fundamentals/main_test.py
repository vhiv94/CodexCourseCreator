"""Lesson-scoped tests for the Personal Tracker fundamentals redesign."""

from __future__ import annotations

from pathlib import Path

import pytest

import main


def require(name: str):
    obj = getattr(main, name, None)
    assert obj is not None, f"Expected `{name}` to exist in main.py."
    return obj


# ============================
# BEGIN LESSON BLOCK: Ch1/L1
# selector: lesson_ch1_l1
# ============================
@pytest.mark.lesson_ch1_l1
def test_welcome_message_contains_personal_tracker() -> None:
    build_welcome_message = require("build_welcome_message")
    message = build_welcome_message()
    assert isinstance(message, str)
    assert "personal tracker" in message.lower()


# ============================
# BEGIN LESSON BLOCK: Ch1/L2
# selector: lesson_ch1_l2
# ============================
@pytest.mark.lesson_ch1_l2
def test_build_app_metadata_returns_named_fields() -> None:
    build_app_metadata = require("build_app_metadata")
    metadata = build_app_metadata()
    assert isinstance(metadata, dict)
    assert {"app_name", "version", "debug_mode"} <= set(metadata)


# ============================
# BEGIN LESSON BLOCK: Ch1/L3
# selector: lesson_ch1_l3
# ============================
@pytest.mark.lesson_ch1_l3
def test_make_starter_profile_uses_str_int_float_bool() -> None:
    make_starter_profile = require("make_starter_profile")
    profile = make_starter_profile("Ava", 1, 2.5, True)
    assert isinstance(profile["username"], str)
    assert isinstance(profile["starting_entries"], int)
    assert isinstance(profile["target_hours"], float)
    assert isinstance(profile["notifications_enabled"], bool)


# ============================
# BEGIN LESSON BLOCK: Ch1/L4
# selector: lesson_ch1_l4
# ============================
@pytest.mark.lesson_ch1_l4
def test_compute_progress_percentage_rounds_two_decimals() -> None:
    compute_progress_percentage = require("compute_progress_percentage")
    assert compute_progress_percentage(3, 4) == 75.0


# ============================
# BEGIN LESSON BLOCK: Ch2/L1
# selector: lesson_ch2_l1
# ============================
@pytest.mark.lesson_ch2_l1
def test_extract_tag_prefix_reads_substring() -> None:
    extract_tag_prefix = require("extract_tag_prefix")
    assert extract_tag_prefix("health:walk", 6) == "health"


# ============================
# BEGIN LESSON BLOCK: Ch2/L2
# selector: lesson_ch2_l2
# ============================
@pytest.mark.lesson_ch2_l2
def test_count_alpha_characters_iterates_string() -> None:
    count_alpha_characters = require("count_alpha_characters")
    assert count_alpha_characters("A1 b2!") == 2


# ============================
# BEGIN LESSON BLOCK: Ch2/L3
# selector: lesson_ch2_l3
# ============================
@pytest.mark.lesson_ch2_l3
def test_normalize_entry_text_trims_and_lowercases() -> None:
    normalize_entry_text = require("normalize_entry_text")
    assert normalize_entry_text("  READ PYTHON  ") == "read python"


# ============================
# BEGIN LESSON BLOCK: Ch2/L4
# selector: lesson_ch2_l4
# ============================
@pytest.mark.lesson_ch2_l4
def test_is_valid_entry_rejects_empty_after_normalization() -> None:
    is_valid_entry = require("is_valid_entry")
    assert is_valid_entry("   ") is False
    assert is_valid_entry("exercise") is True


# ============================
# BEGIN LESSON BLOCK: Ch3/L1
# selector: lesson_ch3_l1
# ============================
@pytest.mark.lesson_ch3_l1
def test_add_entry_returns_new_list_without_mutating_original() -> None:
    add_entry = require("add_entry")
    original = ["walk"]
    updated = add_entry(original, "read")
    assert updated == ["walk", "read"]
    assert original == ["walk"]


# ============================
# BEGIN LESSON BLOCK: Ch3/L2
# selector: lesson_ch3_l2
# ============================
@pytest.mark.lesson_ch3_l2
def test_make_entry_tuple_returns_fixed_order_fields() -> None:
    make_entry_tuple = require("make_entry_tuple")
    entry = make_entry_tuple("run", "health", 30)
    assert isinstance(entry, tuple)
    assert entry == ("run", "health", 30)


# ============================
# BEGIN LESSON BLOCK: Ch3/L3
# selector: lesson_ch3_l3
# ============================
@pytest.mark.lesson_ch3_l3
def test_entry_to_dict_maps_tuple_to_named_keys() -> None:
    entry_to_dict = require("entry_to_dict")
    assert entry_to_dict(("run", "health", 30)) == {
        "name": "run",
        "category": "health",
        "minutes": 30,
    }


# ============================
# BEGIN LESSON BLOCK: Ch3/L4
# selector: lesson_ch3_l4
# ============================
@pytest.mark.lesson_ch3_l4
def test_unique_categories_returns_set_of_names() -> None:
    unique_categories = require("unique_categories")
    categories = unique_categories(
        [("run", "health", 30), ("read", "learning", 20), ("walk", "health", 15)]
    )
    assert categories == {"health", "learning"}


# ============================
# BEGIN LESSON BLOCK: Ch4/L1
# selector: lesson_ch4_l1
# ============================
@pytest.mark.lesson_ch4_l1
def test_format_entry_line_uses_all_parameters() -> None:
    format_entry_line = require("format_entry_line")
    line = format_entry_line(name="run", category="health", minutes=30)
    assert line == "run | health | 30"


# ============================
# BEGIN LESSON BLOCK: Ch4/L2
# selector: lesson_ch4_l2
# ============================
@pytest.mark.lesson_ch4_l2
def test_build_summary_returns_dictionary_not_print_only() -> None:
    build_summary = require("build_summary")
    summary = build_summary([("run", "health", 30), ("read", "learning", 20)])
    assert summary == {"count": 2, "total_minutes": 50}


# ============================
# BEGIN LESSON BLOCK: Ch4/L3
# selector: lesson_ch4_l3
# ============================
@pytest.mark.lesson_ch4_l3
def test_increment_minutes_does_not_rely_on_global_state() -> None:
    increment_minutes = require("increment_minutes")
    assert increment_minutes(10, 5) == 15
    assert increment_minutes(10, 0) == 10


# ============================
# BEGIN LESSON BLOCK: Ch4/L4
# selector: lesson_ch4_l4
# ============================
@pytest.mark.lesson_ch4_l4
def test_prepare_entry_pipeline_normalizes_and_validates() -> None:
    prepare_entry_pipeline = require("prepare_entry_pipeline")
    assert prepare_entry_pipeline("  Read  ", "learning", 25) == (
        "read",
        "learning",
        25,
    )


# ============================
# BEGIN LESSON BLOCK: Ch5/L1
# selector: lesson_ch5_l1
# ============================
@pytest.mark.lesson_ch5_l1
def test_main_module_exposes_importable_public_api_list() -> None:
    public_api = require("PUBLIC_API")
    assert isinstance(public_api, tuple)
    assert "prepare_entry_pipeline" in public_api


# ============================
# BEGIN LESSON BLOCK: Ch5/L2
# selector: lesson_ch5_l2
# ============================
@pytest.mark.lesson_ch5_l2
def test_main_function_is_defined_for_main_guard() -> None:
    run_cli = require("main")
    assert callable(run_cli)


# ============================
# BEGIN LESSON BLOCK: Ch5/L3
# selector: lesson_ch5_l3
# ============================
@pytest.mark.lesson_ch5_l3
def test_plan_main_steps_returns_sequence_order() -> None:
    plan_main_steps = require("plan_main_steps")
    assert plan_main_steps() == [
        "load_entries",
        "handle_command",
        "save_entries",
        "render_output",
    ]


# ============================
# BEGIN LESSON BLOCK: Ch5/L4
# selector: lesson_ch5_l4
# ============================
@pytest.mark.lesson_ch5_l4
def test_dispatch_command_handles_add_list_summary() -> None:
    dispatch_command = require("dispatch_command")
    assert dispatch_command("add") == "add"
    assert dispatch_command("list") == "list"
    assert dispatch_command("summary") == "summary"


# ============================
# BEGIN LESSON BLOCK: Ch6/L1
# selector: lesson_ch6_l1
# ============================
@pytest.mark.lesson_ch6_l1
def test_save_and_load_entries_round_trip(tmp_path: Path) -> None:
    save_entries = require("save_entries")
    load_entries = require("load_entries")
    file_path = tmp_path / "entries.txt"
    save_entries(file_path, ["run|health|30", "read|learning|20"])
    assert load_entries(file_path) == ["run|health|30", "read|learning|20"]


# ============================
# BEGIN LESSON BLOCK: Ch6/L2
# selector: lesson_ch6_l2
# ============================
@pytest.mark.lesson_ch6_l2
def test_append_record_adds_line_without_overwriting(tmp_path: Path) -> None:
    append_record = require("append_record")
    file_path = tmp_path / "entries.txt"
    append_record(file_path, "run|health|30")
    append_record(file_path, "read|learning|20")
    assert file_path.read_text(encoding="utf-8").splitlines() == [
        "run|health|30",
        "read|learning|20",
    ]


# ============================
# BEGIN LESSON BLOCK: Ch6/L3
# selector: lesson_ch6_l3
# ============================
@pytest.mark.lesson_ch6_l3
def test_safe_parse_minutes_returns_default_on_error() -> None:
    safe_parse_minutes = require("safe_parse_minutes")
    assert safe_parse_minutes("12") == 12
    assert safe_parse_minutes("x", default=0) == 0


# ============================
# BEGIN LESSON BLOCK: Ch6/L4
# selector: lesson_ch6_l4
# ============================
@pytest.mark.lesson_ch6_l4
def test_validate_record_line_returns_false_for_bad_shape() -> None:
    validate_record_line = require("validate_record_line")
    assert validate_record_line("run|health|30") is True
    assert validate_record_line("run|health") is False


# ============================
# BEGIN LESSON BLOCK: Ch7/L1
# selector: lesson_ch7_l1
# ============================
@pytest.mark.lesson_ch7_l1
def test_tracker_item_class_exists() -> None:
    tracker_item = require("TrackerItem")
    assert isinstance(tracker_item, type)


# ============================
# BEGIN LESSON BLOCK: Ch7/L2
# selector: lesson_ch7_l2
# ============================
@pytest.mark.lesson_ch7_l2
def test_tracker_item_init_stores_name_category_minutes() -> None:
    tracker_item = require("TrackerItem")
    item = tracker_item("run", "health", 30)
    assert item.name == "run"
    assert item.category == "health"
    assert item.minutes == 30


# ============================
# BEGIN LESSON BLOCK: Ch7/L3
# selector: lesson_ch7_l3
# ============================
@pytest.mark.lesson_ch7_l3
def test_tracker_item_str_and_repr_are_distinct() -> None:
    tracker_item = require("TrackerItem")
    item = tracker_item("read", "learning", 20)
    assert str(item) != ""
    assert repr(item) != ""
    assert str(item) != repr(item)


# ============================
# BEGIN LESSON BLOCK: Ch7/L4
# selector: lesson_ch7_l4
# ============================
@pytest.mark.lesson_ch7_l4
def test_tracker_item_status_line_returns_string() -> None:
    tracker_item = require("TrackerItem")
    item = tracker_item("walk", "health", 15)
    assert isinstance(item.status_line(), str)


# ============================
# BEGIN LESSON BLOCK: Ch8/L1
# selector: lesson_ch8_l1
# ============================
@pytest.mark.lesson_ch8_l1
def test_inheritance_base_and_children_exist() -> None:
    base_tracker_item = require("BaseTrackerItem")
    fitness_item = require("FitnessTrackerItem")
    learning_item = require("LearningTrackerItem")
    assert issubclass(fitness_item, base_tracker_item)
    assert issubclass(learning_item, base_tracker_item)


# ============================
# BEGIN LESSON BLOCK: Ch8/L2
# selector: lesson_ch8_l2
# ============================
@pytest.mark.lesson_ch8_l2
def test_polymorphic_summary_uses_shared_interface() -> None:
    render_item_summaries = require("render_item_summaries")
    base_tracker_item = require("BaseTrackerItem")

    class DemoItem(base_tracker_item):
        def summary(self) -> str:
            return "demo"

    assert render_item_summaries([DemoItem("x", "y", 1)]) == ["demo"]


# ============================
# BEGIN LESSON BLOCK: Ch8/L3
# selector: lesson_ch8_l3
# ============================
@pytest.mark.lesson_ch8_l3
def test_build_tracker_report_integrates_functions_and_objects() -> None:
    build_tracker_report = require("build_tracker_report")
    report = build_tracker_report([("run", "health", 30), ("read", "learning", 20)])
    assert isinstance(report, str)
    assert "run" in report.lower()
    assert "read" in report.lower()


# ============================
# BEGIN LESSON BLOCK: Ch8/L4
# selector: lesson_ch8_l4
# ============================
@pytest.mark.lesson_ch8_l4
def test_run_tracker_session_returns_final_output_string() -> None:
    run_tracker_session = require("run_tracker_session")
    output = run_tracker_session(
        existing_lines=[],
        command="add",
        name="run",
        category="health",
        minutes="30",
    )
    assert isinstance(output, str)
