# Smart Traffic Controller

*Step 8 output: chained from the code in `src/traffic_controller.py`, the tests, and `7_testing_notes.md`.*

## Overview
`TrafficController` chooses which approach (N, E, S, W) of a 4-way intersection gets the next green and for how long. Priority order: **emergency > starved > longest queue**. Green time is proportional to queue length, clamped between a minimum and maximum.

## Install / run
No dependencies (Python 3 standard library).
```
python3 src/traffic_controller.py            # demo
python3 -m unittest discover -s tests        # tests
```

## API
- `TrafficController(min_green=10, max_green=60, seconds_per_vehicle=2.0, max_wait_cycles=3)`. Raises `ValueError` if `min_green <= 0` or `max_green < min_green`.
- `green_time(queue_len: int) -> int`: seconds of green, `int(clamp(queue_len * seconds_per_vehicle, min_green, max_green))`. Negative input raises `ValueError`.
- `next_phase(queues: dict, emergency: str | None = None) -> str`: `queues` must have exactly the keys N, E, S, W. Returns the direction to serve and updates the internal skipped counters. Invalid keys or an unknown emergency direction raise `ValueError`.

Example
```python
c = TrafficController()
q = {"N": 12, "E": 3, "S": 8, "W": 1}
d = c.next_phase(q)          # "N"
c.green_time(q[d])           # 24
```

## Configuration
| Parameter | Default | Meaning |
|---|---|---|
| min_green | 10 | shortest green in seconds |
| max_green | 60 | longest green in seconds |
| seconds_per_vehicle | 2.0 | green seconds granted per queued vehicle |
| max_wait_cycles | 3 | skips after which a non-empty approach is treated as starved |

## Limitations
- Values inside `queues` are not validated in `next_phase`; `seconds_per_vehicle` and `max_wait_cycles` are not validated (see `7_testing_notes.md`).
- Always returns a direction, even when all queues are empty.
- No amber/all-red timing, pedestrian phases, or multi-intersection coordination.
- Not thread-safe; state is in memory only.
- The emergency override is unconditional and does not rate-limit repeated requests.

## Future work
Input validation hardening, idle result for empty queues, pedestrian phases, persistence of counters, demand forecasting, dashboard integration, and the fail-safe fixed-time fallback described in the architecture.
