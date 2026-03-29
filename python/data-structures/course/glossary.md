# Glossary — Inventory Operations Data Structures

Terms below are used throughout the redesigned inventory-operations module.

- **Abstract data type (ADT):** Behavioral contract for a structure (what operations do), independent of one implementation.
- **Allocation map:** Structure mapping open order lines to candidate stock sources.
- **Audit trail:** Ordered history of inventory operations used for debugging, reconciliation, and rollback.
- **Complexity budget:** Practical upper bound on operation cost used to keep planning workflows responsive.
- **Control tower:** The orchestrating service that coordinates ingest, ledger updates, queues, priorities, and reporting.
- **Deterministic tie-break:** Stable secondary ordering rule when primary priorities are equal.
- **Functional pipeline:** Sequence of pure transforms (often map/filter/reduce style) that converts raw inputs to canonical outputs.
- **Heap / priority queue:** Structure that retrieves highest (or lowest) priority items efficiently without full sorting.
- **Inventory event:** Atomic operational record such as receive, reserve, pick, adjust, or transfer.
- **KPI (key performance indicator):** Computed metric for monitoring operations, such as fill rate or restock latency.
- **Linked list:** Node-based sequence where each node references the next node, useful for explicit control over structural updates.
- **LIFO / stack:** Last-in-first-out discipline, used in this module for undo and replay workflows.
- **FIFO / queue:** First-in-first-out discipline, used for fair replenishment and dispatch sequencing.
- **Normalization:** Converting inconsistent raw event data into one canonical shape before business logic.
- **Replay:** Reapplying previously recorded operations in order to reconstruct state after a failure.
- **SKU:** Stock keeping unit; canonical product identifier used across indexing and allocation.
- **State invariant:** Condition that must always remain true (for example, non-negative on-hand counts).
- **Warehouse location:** Storage coordinate or bin identifier used in stock indexing and picking constraints.
