# Reverse prompting - Claude outputs (3 case studies)
Tool: Claude, answered directly. Token counts below are approximate word counts (prompt + output).

## Case 1: Smart Irrigation (model asks questions, does not design yet)
Approx. words (prompt + output): about 190

1. **What do you grow, and on how much land?** (crop types, field size and layout, growth stage, whether zones differ)
2. **What is your water source and current equipment?** (well, canal, tank; pump size and flow rate; drip, sprinkler or flood; any existing valves or controllers)
3. **What soil and climate conditions apply?** (soil type, slope, typical rainfall and heat, how often you see drought or waterlogging)
4. **What budget and maintenance capacity do you have?** (upfront limit, running costs, who repairs it, how technical the user is)
5. **What connectivity and power are available?** (mains, solar, mobile signal or Wi-Fi, LoRa range; whether it must work offline)
6. **What outcomes matter most and what limits apply?** (save water, save labour, raise yield; water-use quotas or fertiliser (fertigation) needs; how much manual override you want and what alerts you need)

## Case 2: Drone Navigation (write the prompt that would produce this output)
Approx. words (prompt + output): about 240

Target output: "Use a PID controller with obstacle repulsive potential fields."

**Best prompt:**
```
You are a control engineer. I have a quadcopter flying from A to B in an environment with obstacles. Recommend a control and avoidance approach, in one or two sentences, that combines a classical feedback controller for tracking with a reactive obstacle-avoidance method. Prefer well-established, lightweight methods that run on a small onboard computer. Answer concisely with the method names and how they connect.
```
**Context the prompt must include (otherwise the answer could just as well be MPC, RRT*, or a learned policy):**
- Vehicle: quadcopter, dynamics and rate of the inner loop, computing budget.
- Sensors available (range/depth, camera, GPS, IMU) and their update rates.
- Environment: static or moving obstacles, indoor or outdoor, density of clutter.
- Task and objective: point-to-point flight, with the safety margin and maximum speed.
- Desired answer style: short, name the algorithms, no derivations.
- Preferences and constraints: prefers classical/explainable methods, lightweight compute, reactive (no global map).
- Known caveat worth asking for: potential fields can get stuck in local minima, so ask the answer to mention it if that is wanted.

## Case 3: Robot Path Planning (reconstruct the requirements prompt)
Approx. words (prompt + output): about 240

**Limitation:** the prompt says "Given this final design document (paste)", but no document was pasted in the repository. I did not invent one. As a stand-in, I used the design decision from Case 3 of the zero-shot and CoT outputs in this exercise (A* with Manhattan heuristic on a 20x20 warehouse grid with static shelves) and reconstructed the likely requirements prompt from it. It is only a plausible reconstruction.

**Reconstructed prompt:**
```
Design the path-planning module for a single warehouse robot operating on a 20x20 grid map with static shelves (no moving obstacles). The robot moves in 4 directions with uniform step cost. It must compute optimal (shortest) paths from any start to any pick location in real time on a small embedded computer. Choose an algorithm, justify it against alternatives (Dijkstra, D* Lite, RRT), specify the heuristic, state the expected node expansions, and note limitations and when the design would need to change (dynamic obstacles, multiple robots, weighted aisles).
```
Requirements that are inferable from such a document: grid size and connectivity, static environment, optimality, real-time limit, single robot, and explicit non-goals (multi-robot, dynamic obstacles).
