# Overview — Python Data Structures (in-memory search index)

## What you build

You implement an **in-memory document mini search stack**: a corpus of documents, a **baseline scan**, then a real **inverted index**, **ordered and prefix-friendly structures**, **ranked top-k results**, and finally **graph-based related-document expansion**. The capstone is one system whose parts compose: linear passes motivate maps; maps motivate ordered trees and tries; scoring motivates heaps; relations motivate adjacency lists and traversals.

## Prerequisites

**Python basics** are assumed: functions, classes, imports, built-in collections (`list`, `dict`, `set`), loops, and simple file-free I/O is not required unless a later lesson explicitly adds it. If you are still shaky on syntax and control flow, complete a fundamentals track first; otherwise Chapter 1 stays review plus API discipline.

## Tooling (uv + pytest)

From `python/data-structures/`:

- Sync the environment: `uv sync`
- Add runtime or dev libraries when lessons call for them: `uv add <package>` (prefer this over ad-hoc `pip install`)
- Run **only** the tests for one lesson selector: `uv run pytest main_test.py -m lesson_ch3_l2`

Configure pytest so imports resolve from your learner package layout—typically a `src/` tree with `pythonpath` set in `pyproject.toml` or `pytest.ini`. Riley’s tests should import **only** learner-facing modules you expose under that layout.

## How the chapters advance the project

- **Ch1 — Sequences and the corpus model:** You represent a corpus as an ordered sequence, iterate deliberately, produce text previews with slicing, and implement naive substring search as the baseline cost story.
- **Ch2 — Stacks, queues, deque:** You use LIFO and FIFO boundaries for real subproblems: query normalization, fair merging of sorted streams, and double-ended sliding when tests require it.
- **Ch3 — Maps, sets, inverted index:** You build term → posting lists, combine postings with set logic for boolean-style queries, and tighten **hashable, stable** keys so dicts and sets behave predictably.
- **Ch4 — Trees:** You add a BST for ordered vocabulary or keys, practice correct insertion under an explicit duplicate policy, then a **trie** for prefix completion over indexed terms.
- **Ch5 — Heaps:** You rank hits with a heap-backed **top-k** flow and make **tie-breaking** deterministic so rankings are reproducible.
- **Ch6 — Graphs:** You model document relationships as an adjacency structure, **expand neighbors breadth-first** within hop limits, then apply **DFS** where the contract needs depth-first structure (components, ordering, or cycle cues per tests).

## End state (behavioral)

By the end, a caller (or tests acting as a caller) can load a corpus representation, **index** it for term lookup, answer **multi-term** queries with intersection semantics where specified, obtain **ordered / prefix** suggestions, fetch **top-k ranked** matches, and **walk a document graph** for related results—each feature grounded in the data structure that earns its place in the design.
