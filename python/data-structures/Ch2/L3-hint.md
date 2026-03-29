# Hints: Compose Stack and Queue in an Intake Service

Use this file only when stuck. It gives direction, not a paste-ready implementation.

**Tests:** `main_test.py` + `lesson_ch2_l3`

## Nudges

1. Define one clear `process_event` contract: return a small dict with stable keys (including whether restock was enqueued).
2. Keep stock updates and side effects in a deterministic order; avoid branching paths that skip audit tracking.
3. Treat reorder checks as data-driven: compare current stock against one threshold boundary every time.

## Algorithm or structure sketch (optional)

```text
receive event
apply stock delta
push event to audit stack
if stock at/below threshold -> enqueue sku
return structured result
```

## Pitfalls to double-check

- Enqueueing before stock is updated can flip boundary outcomes.
- Returning inconsistent result keys makes integration code brittle.
