# Overview

This pilot course applies the redesigned Course Creator flow to a real project: **Kanban Lite API**, a small backend that grows from a local FastAPI service into a self-hosted, operationally sane system. The learner prompt is effectively "I know some Python and want backend fundamentals that lead to a real deployed project," so the course keeps one coherent capstone while narrowing scope to backend foundations rather than trying to cover all of web development at once.

## Intake and generation strategy

The current pilot assumes a learner who is comfortable with basic Python syntax and shell workflows but still needs review on backend mental models such as HTTP contracts, resource ownership, persistence boundaries, and delivery vocabulary.

That assessment drives three decisions:

- the course uses a **module-aware** spine because the subject naturally breaks into delivery foundations, application/data layers, and runtime/operations;
- content is still generated **one chapter at a time** so the course can reassess before the next batch;
- early chapters stay narrow and concrete rather than jumping straight to deployment tooling.

The current authored batch is **Chapter 1**. Later chapters are planned in the spine and `CONTENTS.md`, but they remain future batches rather than pretending the whole course is already fully written.

## What the learner builds

By the end of the full course, Kanban Lite should:

- accept HTTP requests for board, column, and task workflows;
- persist data in SQLite with migration history;
- run in containers with durable storage and reverse-proxy ingress;
- expose operational signals such as logs, health checks, and key metrics;
- support reliability workflows such as rate limiting, backups, restore drills, and CI gates.

## Module arc

- **M1: Request and Delivery Foundations** establishes server/process thinking, HTTP contracts, and how traffic reaches a deployed backend.
- **M2: Application and Data Layers** turns that contract into a maintainable FastAPI service with SQLite-backed data and automated validation.
- **M3: Runtime, Reliability, and Self-Hosting** packages, operates, hardens, and ships the project as a real self-hosted service.

## Prerequisites

- Beginner-level programming comfort and basic Python syntax.
- Ability to run shell commands and edit files from a terminal.
- Willingness to use `uv` for Python dependency and environment management.

## Tooling and workflow

From `python/backend-fundamentals-kanban/`:

```bash
uv sync
uv add <package-name>
uv run pytest main_test.py -m <lesson_selector>
```

Canonical lesson selector format is `lesson_ch<chapter>_l<lesson>` such as `lesson_ch3_l2`.

## Why this course shape works

Kanban Lite is small enough for a beginner-intermediate learner to finish, but rich enough to demonstrate real backend tradeoffs: consistency versus speed, simplicity versus flexibility, and local productivity versus production reliability. The module-aware plan keeps those concerns organized, while chapter batching preserves room for reassessment instead of locking the learner into a rigid one-shot path.
