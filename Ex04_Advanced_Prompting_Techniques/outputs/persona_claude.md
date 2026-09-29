# Persona pattern - Claude outputs (3 case studies)
Tool: Claude, answered directly, role-playing the persona in each prompt. Token counts below are approximate word counts (prompt + output).

## Case 1: Smart Irrigation (agronomist, limited budget)
Approx. words (prompt + output): about 290

Plain advice for tomatoes on a small budget:

**Sensors (cheap first):**
- Two or three soil-moisture probes, one for each part of the plot that behaves differently (sandy corner, low wet spot, main bed), put at root depth, about 15-20 cm. Capacitive ones last longer than the cheapest resistive ones, which corrode.
- A simple rain gauge (a straight-sided jar works) instead of a weather service.
- Optional later: a low-cost timer/controller with a solenoid valve.
- Skip fancy sensors (EC, leaf wetness) until the basics pay off.

**Schedule (adjust to your soil):**
- Drip lines, early morning, so water is not lost to heat and leaves stay dry (less blight).
- Seedlings to first flowers: short, frequent watering to keep the soil evenly damp. Flowering and fruiting: deeper watering, roughly every 2-3 days in loam, more often in sand. Stay steady, because swings in moisture cause cracked fruit and blossom-end rot.
- Rule of thumb: water when the probe reads dry at root depth, or when the top 5 cm feels dry but 10 cm down is still cool and damp. Skip after 10 mm or more of rain. Cut back in cool cloudy weeks.
- Mulch (straw) saves a lot of water and costs almost nothing.

Start with hand valves and the probes; add the automatic timer once you trust the readings. (Any numbers here are rules of thumb, not measured values for your farm.)

## Case 2: Drone Navigation (UAV flight-controller engineer)
Approx. words (prompt + output): about 290

Review of "Use GPS only for obstacle avoidance": **reject**. GPS tells you where you are, not what is in front of you.

Failure modes:
1. GPS knows nothing about obstacles that are not on a map: people, birds, wires, other drones, cranes, moving vehicles.
2. Position accuracy is metres, with a refresh of only a few Hz. That is too coarse and too slow for close avoidance.
3. Dropouts and degradation: urban canyons, trees, indoors, bridges, multipath, and jamming or spoofing. A spoofed drone will confidently fly into things.
4. Altitude error is worse than horizontal error, so vertical separation is unreliable.
5. Latency and an uncertain map: even with a map, out-of-date data (new construction) is a hazard.
6. No fail-safe behaviour defined when GPS is lost.

Fixes:
- Add perception: obstacle sensing with at least one, ideally two, independent modalities (stereo or depth camera, lidar or radar, ultrasonic/ToF for close range).
- Sensor fusion (EKF) with IMU, barometer and optical flow, so state estimation does not depend on GPS alone.
- Detect GPS quality (HDOP, satellite count, innovation checks) and spoofing plausibility checks.
- Geofence, altitude margins and a terrain/obstacle database as a prior only.
- Defined degraded modes: on GPS loss, switch to visual-inertial navigation, slow down, hold or land, then return-to-launch only if the path is validated.
- Verification: hardware-in-the-loop and failure-injection tests, and a conservative speed limit tied to sensing range (stopping distance below detection range).

## Case 3: Robot Path Planning (robotics professor grading BFS plan)
Approx. words (prompt + output): about 260

**Feedback (grade: partial credit).** BFS is a sound algorithm for the right problem, but it is the wrong tool here. BFS minimises the number of steps, not the total cost. In a warehouse with weighted costs (congested aisles, turns, one-way lanes, travel through restricted zones), a route with the fewest cells can be expensive. Your plan would return a path that is short in hops but not in cost, and you should tell me you understand that.

**What earns full credit:**
1. State the objective explicitly: minimise a cost function (distance plus turn penalty plus congestion).
2. Use **Dijkstra** if you have no useful heuristic, or **A\*** with an admissible heuristic (for example, Manhattan distance scaled by the minimum edge cost), which keeps optimality and reduces expansions.
3. If aisle costs or blocked cells change (other robots, pallets), use **D\* Lite** to repair the plan incrementally.
4. Note the multi-robot issue (deadlocks, priorities or reservation tables) and dimension your grid resolution against the robot footprint (inflate obstacles).
5. Give a complexity comment (O(E + V log V) for Dijkstra with a heap) and a test with a case where BFS and Dijkstra disagree.

One small credit-worthy point: if all costs were uniform, BFS and Dijkstra would coincide, so BFS is fine there.
