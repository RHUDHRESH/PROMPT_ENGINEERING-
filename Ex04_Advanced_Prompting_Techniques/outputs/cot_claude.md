# Chain of Thought - Claude outputs (3 case studies)
Tool: Claude, answered directly. Token counts below are approximate word counts (prompt + output).

## Case 1: Smart Irrigation
Approx. words (prompt + output): about 120

1. Water needed: 4 mm over 1 m² is 4 L, so 2000 m² x 4 mm = 8000 L.
2. Rain credit: 1 mm over 2000 m² = 2000 L.
3. Remaining: 8000 - 2000 = 6000 L.
4. Pump time: 6000 L / 30 L/min = 200 min.

**Answer: 200 minutes** (3 h 20 min). Assumes the forecast rain is fully effective, and no losses.

## Case 2: Drone Navigation
Approx. words (prompt + output): about 210

Given: v = 6 m/s, obstacle 30 m ahead, detection delay 0.5 s, deceleration 4 m/s².

1. Distance during the delay (no braking yet): 6 x 0.5 = 3 m.
2. Braking time: 6 / 4 = 1.5 s.
3. Braking distance: v²/(2a) = 36 / 8 = 4.5 m.
4. Total stopping distance: 3 + 4.5 = **7.5 m**, which is less than 30 m, so **the drone stops in time**, with a 22.5 m margin.

Inconsistency in the prompt: "needs 2.5 s to stop" does not match the numbers. Delay plus braking is 0.5 + 1.5 = 2.0 s in total, not 2.5 s. I used the physics (4 m/s² from 6 m/s) rather than the 2.5 s. Even if the 2.5 s were true and the drone flew at full speed for the entire 2.5 s, it would cover at most 6 x 2.5 = 15 m, still under 30 m. So the conclusion holds either way.

## Case 3: Robot Path Planning
Approx. words (prompt + output): about 320

Setup: 100x100 grid = 10,000 cells, 4-connectivity, every step costs 1. Worst-case start (0,0) to goal (99,99): shortest length d = 198 steps.

1. **Dijkstra** with uniform cost behaves like BFS. It expands nodes in order of distance from the start, so it expands every cell with distance < d, a diamond that here covers essentially the entire grid: about 10,000 expansions in the worst case (about half the grid for a goal in the middle). It has no direction knowledge.
2. **A\*** with Manhattan heuristic h = |dx| + |dy| is admissible and consistent for 4-connectivity, so it is still optimal. It expands only nodes with f = g + h <= d. In an obstacle-free grid every monotone path has f = d exactly, so if ties are broken arbitrarily A\* may still expand up to the whole rectangle between start and goal (up to about 10,000 cells in this worst case). With tie-breaking toward larger g (or a tiny heuristic weight), it expands about the path length, roughly 200 nodes. With obstacles, A\* expands more, but still typically far fewer than Dijkstra.
3. **Effect of the heuristic:** it reorients the search toward the goal. The price is a small per-node overhead (computing h and a priority queue), so the gain is largest when the goal is far and the map is fairly open. If the heuristic were 0, A\* equals Dijkstra.

**Recommendation: A\* with Manhattan distance and larger-g tie-breaking.** Same optimal path, far fewer expansions. Dijkstra is only preferable if costs are unknown or there are many goals (one search from the start reaches all).
