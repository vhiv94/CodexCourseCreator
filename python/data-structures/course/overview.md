# Overview — Python Data Structures (Inventory Operations Control Tower)

## What you build

You build an **inventory operations control tower** for a warehouse-style workflow. The system ingests stock movement events, normalizes them through functional pipelines, maintains current stock views, schedules replenishment work, supports undo/recovery operations, and produces KPI reports for daily operations.

This capstone is intentionally realistic: the same event can affect availability, restock urgency, and downstream picking decisions. Data structures are chosen because each one solves a concrete operational problem, not because it is academically interesting on its own.

## Prerequisites

This module assumes you already know Python basics and are comfortable using:

- built-in collections: `list`, `dict`, `set`, `tuple`
- functional helpers: `map`, `filter`, `reduce`
- class and function definitions, plus basic unit testing workflow

You do **not** need prior experience implementing custom data structures from scratch; that is part of the module.

## Tooling (uv + pytest)

From `python/data-structures/`:

- Sync environment and lock dependencies: `uv sync`
- Add packages when needed: `uv add <package>`
- Run one lesson contract at a time: `uv run pytest main_test.py -m <lesson_selector>`

Example:

```text
uv run pytest main_test.py -m lesson_ch2_l1
```

## How the chapters advance the project

- **Ch1 — Inventory Event Modeling and Functional Pipelines:** Define canonical event records and build pure map/filter/reduce transforms for ingest quality.
- **Ch2 — OOP Service Primitives with Stack and Queue:** Implement custom `AuditStack` and `ReplenishmentQueue` classes, then compose them in an intake coordinator.
- **Ch3 — Linked Structures for Movement Ledgers:** Build linked-list classes for movement history and perform safe structural mutations and traversals.
- **Ch4 — Allocation and Picking Workflows:** Use dict and set indexing to match inventory to open orders and generate queue-based wave plans.
- **Ch5 — Prioritization and Throughput Strategy:** Introduce heap-backed urgency selection, deterministic tie-break rules, and complexity-budget reasoning.
- **Ch6 — End-to-End Control Tower Integration:** Integrate all modules into a single service and add functional KPI reporting plus failure-recovery simulation.

## Architectural style goals

The module deliberately combines two styles:

- **OOP style:** encapsulate stateful behavior in classes (`AuditStack`, `ReplenishmentQueue`, linked ledger, orchestrator service).
- **Functional style:** keep transformation/reporting steps pure where possible (normalization, filtering, aggregation, reporting).

Students should be able to explain when each style improves maintainability, correctness, and testability.

## End state (behavioral)

By the end, a caller can submit inventory events, retrieve consistent stock views, schedule and prioritize replenishment, inspect movement history, recover from operational faults through undo/replay semantics, and generate KPI summaries. The complete behavior is validated lesson-by-lesson through selector-scoped tests in `main_test.py`.
