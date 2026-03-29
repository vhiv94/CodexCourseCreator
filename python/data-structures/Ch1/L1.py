"""Ch1/L1 — Represent Documents as a Sequenced Corpus: ordered list, stable ids, retrievable text."""

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
            "Expected an importable learner module at src/corpus.py (package root on sys.path). "
            "Implement build_corpus(...) and get_document_text(..., doc_id). "
            f"Original import error: {exc}"
        )
    return corpus_mod


@pytest.fixture(scope="module")
def corpus_mod():
    return _load_corpus_module()


def test_build_corpus_returns_list_preserving_stable_ids_in_order(corpus_mod) -> None:
    """Spine: ordered sequence; ids stay in the logical order supplied."""
    documents = [(10, "alpha"), (2, "bravo"), (7, "charlie")]
    result = corpus_mod.build_corpus(documents)
    assert isinstance(result, list), "The corpus must stay a Python list (ordered sequence)."
    assert [(pair[0], pair[1]) for pair in result] == [
        (10, "alpha"),
        (2, "bravo"),
        (7, "charlie"),
    ]


def test_get_document_text_retrieves_expected_bodies(corpus_mod) -> None:
    """Spine project_step: ids remain retrievable for later indexing."""
    c = corpus_mod.build_corpus([(1, "first body"), (42, "second body")])
    assert corpus_mod.get_document_text(c, 1) == "first body"
    assert corpus_mod.get_document_text(c, 42) == "second body"


def test_duplicate_doc_ids_are_rejected(corpus_mod) -> None:
    """Stable ids require uniqueness across the corpus."""
    with pytest.raises(ValueError):
        corpus_mod.build_corpus([(1, "a"), (1, "b")])


def test_unknown_doc_id_raises_key_error(corpus_mod) -> None:
    c = corpus_mod.build_corpus([(5, "only")])
    with pytest.raises(KeyError):
        corpus_mod.get_document_text(c, 99)


def test_build_corpus_defensive_copy_of_input_list(corpus_mod) -> None:
    """Mutation of the caller's list after building must not reshuffle stored documents."""
    documents = [(3, "x")]
    corpus = corpus_mod.build_corpus(documents)
    documents.append((4, "y"))
    assert len(corpus) == 1
    assert corpus_mod.get_document_text(corpus, 3) == "x"
    with pytest.raises(KeyError):
        corpus_mod.get_document_text(corpus, 4)


def test_tuple_content_not_aliased_to_caller_mutations(corpus_mod) -> None:
    """Once built, swapping entries in the input list must not change retrieved text."""
    rows = [(1, "original")]
    corpus = corpus_mod.build_corpus(rows)
    rows[0] = (9, "replaced")
    assert corpus_mod.get_document_text(corpus, 1) == "original"


# Canonical runner (from python/data-structures/):
#   uv run pytest Ch1/L1.py
