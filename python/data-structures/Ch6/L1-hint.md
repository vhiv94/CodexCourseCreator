# Hints: Compose an InventoryControlTower Service

Use this file only when stuck. It helps with orchestration boundaries, not full service code.

**Tests:** `main_test.py` + `lesson_ch6_l1`

## Nudges

1. Keep constructor dependencies explicit (stock state, queue/stack behavior, threshold config).
2. In batch processing, apply each event through the same pipeline path to avoid divergent side effects.
3. Snapshot should be a coherent external view of current state, not an internal debug dump.

## Algorithm or structure sketch (optional)

```text
for event in batch:
  process event through coordinator flow
collect processed count
expose snapshot with stock + pending restock
```

## Pitfalls to double-check

- Updating snapshot fields from stale pre-event state.
- Hiding side effects in helper calls that bypass contract logic.
