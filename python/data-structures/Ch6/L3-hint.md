# Hints: Simulate Failure Recovery with Undo and Replay

Use this file only when stuck. It provides recovery design cues, not complete runnable code.

**Tests:** `main_test.py` + `lesson_ch6_l3`

## Nudges

1. Make `fail_after` behavior explicit and repeatable so the same input always fails at the same point.
2. Track at least three outcomes: recovered status, final processed count, replay count.
3. Keep replay logic idempotence-aware: avoid counting duplicated work as successful new processing.

## Algorithm or structure sketch (optional)

```text
process events until failure point
capture partial state and remaining work
replay required operations deterministically
return recovery summary metrics
```

## Pitfalls to double-check

- Off-by-one logic around the failure boundary.
- Reporting replay count inconsistently with actual replay attempts.
