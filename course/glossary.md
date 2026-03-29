# Glossary — Data structures course

Terms below are course-facing shorthand; precise meanings in your code should match Riley’s tests and each lesson’s contract.

- **Abstract data type (ADT):** A behavioral specification (operations + expected semantics) independent of one concrete implementation.
- **Adjacency list:** A graph representation mapping each node to its neighbors (and optional edge weights), usually sparse.
- **Amortized cost:** Average cost per operation over a sequence; individual steps may be expensive but the long-run average is low (often cited for dynamic tables and some tree rebalances—here, main ideas only).
- **Balanced delimiter / nesting:** Structure in token streams where a stack records “what is still open” so closing symbols match in LIFO order.
- **Breadth-first search (BFS):** Explore a graph layer-by-layer using a queue frontier; finds shortest hop count in unweighted graphs.
- **BST invariant:** For each node, keys in the left subtree are ordered before the node’s key, and keys in the right subtree after—per the lesson’s compare rule.
- **Corpus:** The ordered collection of documents your indexer treats as the universe of searchable text.
- **Deque:** Double-ended queue—O(1) append/pop at both ends in the standard library’s `collections.deque`.
- **Depth-first search (DFS):** Go deep before wide; commonly recursion or an explicit stack; ordering and edge classification depend on the stated traversal rule.
- **Hashable:** A value usable as a `dict` key or `set` element—immutable built-ins and tuples of hashables, with consistent `__hash__` and `__eq__`.
- **Heap / priority queue:** Tree-shaped priority discipline; Python’s `heapq` implements a min-heap on a list with sift operations.
- **Inverted index:** Mapping from a **term** to the **list (or set) of documents** where the term occurs—classic text-retrieval structure.
- **Posting list:** The list of document ids associated with a term in an inverted index (often kept sorted for merging).
- **Prefix tree (trie):** Tree whose paths spell tokens or characters; supports prefix queries by walking from the root.
- **Queue (FIFO):** First-in-first-out discipline—fair scheduling and BFS frontiers.
- **Stack (LIFO):** Last-in-first-out discipline—nesting, reversal, and some DFS implementations.
- **Top-k:** The k highest-scoring items by a ranking rule, often maintained with a heap to avoid sorting everything.
- **Tie-break:** Secondary comparison when primary scores match—here, typically a stable rule such as document id order.
