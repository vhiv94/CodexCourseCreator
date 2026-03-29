# Overview

This course teaches backend fundamentals by building and self-hosting a single coherent project: **Kanban Lite API**. You will learn what a server is, how DNS routes users to your service, how relational storage works with SQLite, and how to package and run the system in Docker containers on a VPS.

By the end, the system behavior is:

- Accept HTTP requests for board, column, and task workflows.
- Persist data in SQLite with migration history.
- Run in containers with durable storage and reverse-proxy ingress.
- Expose operational signals (logs, health, key metrics).
- Support reliability workflows (rate limiting, backups, restore drills, and CI gates).

## Prerequisites

- Beginner-level programming comfort and basic Python syntax.
- Ability to run shell commands and edit files from a terminal.
- Willingness to use uv for Python dependency and environment management.

## Tooling and workflow (uv)

From `python/backend-fundamentals-kanban/`:

```bash
uv sync
uv add <package-name>
uv run pytest main_test.py -m <lesson_selector>
```

Canonical lesson selector format is `lesson_ch<chapter>_l<lesson>` (for example `lesson_ch3_l2`).

## Course arc by chapter

- **Ch1: Server and HTTP Fundamentals** builds your core mental model of server processes, request-response contracts, and API consistency.
- **Ch2: DNS and Internet Delivery** explains how traffic reaches your backend and how to troubleshoot delivery failures.
- **Ch3: SQLite Data and Migrations** turns project requirements into schema, constraints, indexes, and migration-safe change workflows.
- **Ch4: FastAPI Architecture and Testing** structures the application into maintainable layers and validates behavior with automated tests.
- **Ch5: Containers and Runtime** packages the app for reproducible execution, networking, and durable data in containerized environments.
- **Ch6: Production Backend Essentials** adds caching, background jobs, observability, and baseline security/rate limiting controls.
- **Ch7: Self-Hosting Reliability and CI CD** operationalizes deployment, recovery, and release automation into a maintainable runbook.

## Why this project shape works

Kanban Lite is small enough for a beginner-intermediate learner to finish, but rich enough to demonstrate real backend tradeoffs: consistency vs speed, simplicity vs flexibility, and local productivity vs production reliability. Skills learned here transfer directly to other backend domains such as note apps, content backends, internal tools, and API-first products.
