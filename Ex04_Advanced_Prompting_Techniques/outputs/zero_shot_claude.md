# Zero-shot - Claude outputs (3 case studies)
Tool: Claude, answered directly. Token counts below are approximate word counts (prompt + output), a proxy only.

## Case 1: Smart Irrigation
Approx. words (prompt + output): about 230

```
# Inputs: moisture (%), rain_mm (forecast, next 24 h), temp_c
# Tunable constants
DRY = 25          # % below which the crop is stressed
WET = 45          # % above which watering is never needed
RAIN_SKIP = 5     # mm of forecast rain that is enough to skip
HOT = 30          # deg C

function decide(moisture, rain_mm, temp_c):
    if moisture >= WET:
        return SKIP
    if rain_mm >= RAIN_SKIP and moisture >= DRY:
        return SKIP                      # rain will cover the need
    if moisture < DRY:
        minutes = base_minutes
        if temp_c >= HOT: minutes = minutes * 1.3   # more evaporation
        minutes = minutes - rain_mm * minutes_per_mm  # credit forecast rain
        return WATER(max(minutes, min_run))
    # moderate zone: DRY <= moisture < WET
    if temp_c >= HOT and rain_mm < 1:
        return WATER(short)
    return SKIP
# Extra rules: never water within 1 h of measured rain, cap daily runtime,
# fall back to a time schedule if the moisture sensor value is missing or out of range.
```
The thresholds are illustrative and must be calibrated per soil and crop.

## Case 2: Drone Navigation
Approx. words (prompt + output): about 280

1. **Estimate own motion (IMU + camera).** Fuse IMU (accelerometer and gyro) with visual odometry (feature tracking) in an EKF to get pose and velocity. Without GPS, the camera corrects IMU drift; the IMU covers gaps between frames.
2. **Detect the obstacle.** Run an object detector or optical-flow / motion segmentation on each frame. A monocular camera has no direct depth, so estimate range from the obstacle's apparent size growth (looming / time-to-contact) or from motion parallax as the drone moves.
3. **Track and predict.** Keep a Kalman-filter track of the obstacle's bearing and range and extrapolate a short horizon (1-3 s) to predict where it will be, with an uncertainty envelope.
4. **Plan.** Follow a straight-line or waypoint path A to B. When the predicted obstacle envelope crosses the path within the time-to-contact threshold, generate an avoidance manoeuvre (lateral or vertical offset away from the obstacle's motion, using a velocity-obstacle or potential-field method), then blend back to the A-B line.
5. **Control.** A cascaded PID/MPC controller turns the reference velocity into attitude commands, with speed limits so stopping distance is shorter than the detection range.
6. **Safety.** If tracking is lost or the estimate is uncertain, slow or hover, and use a simple rule such as "obstacle in view and growing means move away". The key limitation is scale ambiguity of a single camera, so use conservative margins.

## Case 3: Robot Path Planning
Approx. words (prompt + output): about 170

**Choice: A\* with a Manhattan-distance heuristic (4-connected grid), on a precomputed occupancy grid.**

Why: a 20x20 grid has only 400 cells, static shelves mean the map never changes, and A\* is optimal (with an admissible heuristic) while expanding far fewer nodes than Dijkstra or BFS. Manhattan distance is admissible and consistent for 4-connectivity, so the first time the goal is popped the path is optimal. It is simple to implement and debug. Alternatives: Dijkstra is correct but explores more; D\* Lite only pays off when obstacles appear or move; RRT/PRM target continuous, high-dimensional spaces. Caveat: if aisles have costs (one-way lanes, congestion) or many robots, add cost weights and a multi-robot layer (for example, reservation tables).
