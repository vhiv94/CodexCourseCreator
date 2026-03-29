# Hints: Insert and Remove Ledger Entries Safely

Use this file only when stuck. It gives structural nudges, not a full linked-list solution.

**Tests:** `main_test.py` + `lesson_ch3_l2`

## Nudges

1. Handle head-removal as a distinct branch before middle/tail logic.
2. Track a `previous` pointer while traversing; rewiring `previous.next` is the key operation for middle removal.
3. If the removed node is tail, update tail to the predecessor.

## Algorithm or structure sketch (optional)

```text
walk nodes until predicate matches
rewire links based on node position (head/middle/tail)
decrement length exactly once
return removed value
```

## Pitfalls to double-check

- Forgetting to update tail when removing the last node.
- Decrementing length when no node matched.
