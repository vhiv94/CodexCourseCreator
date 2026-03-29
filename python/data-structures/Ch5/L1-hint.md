# Hints: Rank Restock Tasks with a Heap

Use this file only when stuck. It explains priority-queue direction, not a full implementation.

**Tests:** `main_test.py` + `lesson_ch5_l1`

## Nudges

1. Decide clearly whether your heap logic is max-priority or min-priority, then transform keys consistently.
2. Validate behavior first with tiny datasets where expected top-k is obvious.
3. Separate "candidate selection" from "final returned ordering" if needed for readability.

## Algorithm or structure sketch (optional)

```text
build heap entries from tasks using priority key
extract up to k tasks
return in expected ranked order
```

## Pitfalls to double-check

- Mixing ascending/descending assumptions between heap key and output.
- Returning more than `k` elements when input is large.
