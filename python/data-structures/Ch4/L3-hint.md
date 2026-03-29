# Hints: Queue-Driven Picking Wave Planner

Use this file only when stuck. It provides planning heuristics, not full code.

**Tests:** `main_test.py` + `lesson_ch4_l3`

## Nudges

1. Preserve source order exactly; avoid sorting unless the contract explicitly asks for it.
2. Keep one `current_wave` buffer and flush it when it reaches `max_wave_size`.
3. After processing all picks, flush a non-empty partial final wave.

## Algorithm or structure sketch (optional)

```text
for each pick in picks:
  append to current wave
  if wave full: emit and reset
after loop: emit remainder if present
```

## Pitfalls to double-check

- Dropping the last partial wave.
- Mutating original pick rows when grouping waves.
