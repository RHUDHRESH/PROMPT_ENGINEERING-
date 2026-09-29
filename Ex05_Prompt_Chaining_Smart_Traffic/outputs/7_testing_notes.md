# Step 7 - Testing notes: coverage and uncovered edge cases

The tests themselves live in `tests/test_traffic_controller.py` (6 tests, all passing with `python3 -m unittest discover -s tests`).

## What is covered
green_time bounds (0, 100, 15), negative queue in green_time, longest queue first, emergency pre-emption, starvation (small queue served within 5 cycles), wrong queue keys, invalid min_green.

## Edge cases NOT covered by the current tests
The behaviours below were checked by hand against the current code (observed results in brackets), but no test asserts them.

1. All-zero queues: `next_phase` still returns a direction ("N" by tie order) and no "idle" result exists.
2. Tie-breaking: equal queues resolve in N,E,S,W order; not asserted.
3. Negative values inside `next_phase` queues are not validated (all -ve queues returned "E", the least negative). Only `green_time` rejects negatives.
4. Non-integer queue values: `green_time(2.5)` and `green_time(True)` are accepted (both returned 10).
5. Non-numeric queue values (None, str) and non-dict `queues` types.
6. Unknown emergency direction (`emergency="X"`) raising ValueError; and lowercase "n".
7. Emergency does not check queue length: an emergency on an empty approach still gets the green.
8. Repeated emergencies: skipped counters of other approaches keep growing (after 4 emergencies on W, N and E were both starved).
9. Starvation exact boundary: served on exactly the `max_wait_cycles`-th skip. Observed pattern with N=50, E=1: N,N,N,E,N,N,N,E.
10. Starved approach with empty queue must not be picked; starved-tie resolution among several starved approaches.
11. `max_wait_cycles=0` (every non-empty approach counts as starved, so effectively longest-queue) and negative values are not validated.
12. `seconds_per_vehicle <= 0` is not validated: with -1, green_time(5) returned min_green (10).
13. `max_green < min_green` case (only min_green=0 is tested).
14. Exact clamp boundaries (queue 5 -> 10 s, queue 30 -> 60 s) and int truncation for fractional factors.
15. Controller state persistence across many cycles, and thread safety (no locking; not tested or supported).
16. Missing tests for the `__main__` demo.
