"""Ch1/L2 — Walk the Corpus with Control: intentional list iteration, enumerate, summary stats."""

from __future__ import annotations

import sys
from pathlib import Path

import pytest

_COURSE_ROOT = Path(__file__).resolve().parents[1]
_SRC = _COURSE_ROOT / "src"
if str(_SRC) not in sys.path:
    sys.path.insert(0, str(_SRC))


def _load_corpus_module():  # pragma: no cover - import guard for learner wiring
    try:
        import corpus as corpus_mod  # type: ignore[import-not-found]
    except ImportError as exc:
        pytest.fail(
            "Expected an importable learner module at src/corpus.py. "
            "Keep Ch1/L1 helpers and add summarize_corpus(corpus). "
            f"Original import error: {exc}"
        )
    return corpus_mod


@pytest.fixture(scope="module")
def corpus_mod():
    return _load_corpus_module()


def test_corpus_exposes_summarize_corpus_callable(corpus_mod) -> None:
    assert hasattr(corpus_mod, "summarize_corpus"), (
        "Add summarize_corpus(corpus) -> tuple[int, list[int], int] to src/corpus.py: "
        "(document_count, body_lengths in corpus order, total_characters)."
    )
    assert callable(corpus_mod.summarize_corpus), "summarize_corpus must be callable."


def _get_summarize_or_skip(corpus_mod):
    if not hasattr(corpus_mod, "summarize_corpus"):
        pytest.skip(
            "Behavior checks require summarize_corpus; see "
            "test_corpus_exposes_summarize_corpus_callable for the contract."
        )
    return corpus_mod.summarize_corpus


@pytest.mark.parametrize(
    ("documents", "expected_lengths"),
    [
        ([], []),
        ([(1, "aa"), (2, "bbb"), (3, "")], [2, 3, 0]),
    ],
)
def test_summarize_contract_for_counts_lengths_and_total(
    corpus_mod, documents, expected_lengths
) -> None:
    summarize_corpus = _get_summarize_or_skip(corpus_mod)
    corpus = corpus_mod.build_corpus(documents)
    summary = summarize_corpus(corpus)

    assert isinstance(summary, tuple), "summarize_corpus must return a tuple."
    assert len(summary) == 3, "Expected (document_count, body_lengths, total_characters)."

    n_docs, lengths, total_chars = summary
    assert n_docs == len(expected_lengths)
    assert lengths == expected_lengths
    assert total_chars == sum(expected_lengths)


def test_summarize_reported_count_matches_length_list_size(corpus_mod) -> None:
    summarize_corpus = _get_summarize_or_skip(corpus_mod)
    corpus = corpus_mod.build_corpus([(1, "aa"), (2, "bbb"), (3, "")])
    n_docs, lengths, total_chars = summarize_corpus(corpus)
    assert n_docs == 3
    assert n_docs == len(lengths)
    assert total_chars == sum(lengths)


def test_length_sequence_follows_corpus_sequence_not_just_multiset(corpus_mod) -> None:
    """Same bodies in different list positions yield different ordered length runs."""
    summarize_corpus = _get_summarize_or_skip(corpus_mod)
    first = corpus_mod.build_corpus([(10, "x"), (20, "yy")])
    second = corpus_mod.build_corpus([(20, "yy"), (10, "x")])
    _, lengths_a, _ = summarize_corpus(first)
    _, lengths_b, _ = summarize_corpus(second)
    assert lengths_a == [1, 2]
    assert lengths_b == [2, 1]


def test_summarize_corpus_does_not_mutate_input_corpus(corpus_mod) -> None:
    summarize_corpus = _get_summarize_or_skip(corpus_mod)
    corpus = corpus_mod.build_corpus([(1, "alpha"), (2, "beta")])
    before = list(corpus)
    _ = summarize_corpus(corpus)
    assert corpus == before


# Canonical runner (from python/data-structures/):
#   uv run pytest Ch1/L2.py
