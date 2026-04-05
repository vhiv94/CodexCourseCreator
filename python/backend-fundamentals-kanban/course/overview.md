# Overview

This pilot course applies the redesigned Course Creator flow to a real project: **Kanban Lite API**, a small backend that grows from a local FastAPI service into a self-hosted, operationally sane system. A refreshed intake confirmed that the learner still wants a backend-first project that ends in self-hosting, so the course keeps one coherent capstone while narrowing scope to backend foundations rather than trying to cover all of web development at once.

## Intake and generation strategy

The refreshed intake shows a learner who is comfortable with everyday Python and shell workflows, but who wants real depth in backend thinking. Python syntax can stay in review mode, while HTTP/API concepts and relational data modeling need first-class teaching attention.

That assessment drives three decisions:

- the course keeps **Kanban Lite API** as the capstone because the learner still wants a deployable backend project rather than a different app direction;
- the course keeps a **module-aware** spine because the subject still breaks cleanly into delivery foundations, application/data layers, and runtime/operations;
- content is still generated **one chapter at a time** so the course can reassess before the next batch instead of assuming later infrastructure work is ready immediately.

The first authored sequence remains **Chapter 1**. Its narrow readiness checkpoint at `course/M1/Ch1/ASSESSMENT.md` is now complete, and it confirmed that the numbered Chapter 1 batch should be taught as guided review rather than assumed prior knowledge. The real Chapter 1 lessons still keep their logical ids `Ch1/L1` through `Ch1/L4`, while their on-disk lesson files live under `course/M1/Ch1/` so the module-aware layout matches the spine. Later chapters are planned in the spine and `CONTENTS.md`, but they remain future batches rather than pretending the whole course is already fully written.

## Intake snapshot

- **Review heavily:** HTTP request/response flow, API route design, resource ownership, relational schemas, and SQL constraints.
- **Review especially explicitly in Chapter 1:** what a request is asking for, why JSON is the machine-readable default, how nested routes express ownership, which common status/error codes mean what, and what SQLite is persisting after successful writes.
- **Review with practical reinforcement:** deployment vocabulary such as DNS, reverse proxy, containers, VPS, and health checks.
- **Deepen:** FastAPI architecture, persistence boundaries, and end-to-end backend troubleshooting.
- **Pacing note:** operational confidence is still early, so the course should stay guided without becoming low-challenge.

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
