# Step 4 - Signal-timing algorithm

*Chained from `3_architecture.md` (decision engine component).*

Parameters: `min_green=10`, `max_green=60`, `seconds_per_vehicle=2.0`, `max_wait_cycles=3`. State: `skipped[d]` for d in {N,E,S,W}, initially 0.

## green_time(queue_len)
1. If `queue_len < 0`, raise an error.
2. `raw = queue_len * seconds_per_vehicle`.
3. Return `int(max(min_green, min(max_green, raw)))`.

## next_phase(queues, emergency=None)
1. If the keys of `queues` are not exactly {N,E,S,W}, raise an error.
2. If `emergency` is given:
   1. If it is not one of N,E,S,W, raise an error.
   2. Return `serve(emergency)`.
3. `starved` = all d with `skipped[d] >= max_wait_cycles` AND `queues[d] > 0`.
4. If `starved` is non-empty, return `serve(` the starved direction with the largest queue `)`.
5. Otherwise return `serve(` the direction with the largest queue; ties broken by order N,E,S,W `)`.

## serve(direction)
1. For each d: if d == direction, `skipped[d] = 0`; else `skipped[d] += 1`.
2. Return `direction`.

## Complexity
Direction count is a constant (4), so each call is O(1) time and O(1) space. Generalised to k approaches: `next_phase` is O(k), `green_time` O(1).

Note: the skipped counter also increments for empty approaches; only those with `queues[d] > 0` qualify as starved.
