# Active prompting - Claude outputs (3 case studies)
Tool: Claude, answered directly. Token counts below are approximate word counts (prompt + output).

**IMPORTANT - THIS IS A SIMULATION.** Active prompting needs 5 real independent samples per question (fresh runs with sampling temperature) and a human-written exemplar. I cannot run 5 independent samples of myself inside one response, and this repository has no logs of such runs. So for each case I reasoned about which parts of the question are ambiguous and where a model's answers would plausibly diverge, and wrote 5 "samples" that represent that reasoning. The sample counts (e.g., 4 RETURN / 1 CONTINUE) are my estimate of the likely spread, not measured frequencies. The exemplars are written by me (Claude) as a stand-in for the human-written exemplar the method calls for, and the "after exemplar" consistency is a projection, not an experiment. Treat all agreement numbers as illustrative; re-run with real samples before drawing conclusions.

## Case 1: Drone (continue or return)
Approx. words (prompt + output): about 450

**Step 1 - simulated 5 samples**
Question: 20 min battery, 1 kg payload, 6 km from base, 8 m/s headwind. CONTINUE or RETURN?
Where answers would vary: the prompt gives no airspeed, no remaining mission distance, and no direction for the headwind (on the way out or the way home?). Samples would differ on these assumptions.

| # | Answer | One-line reason (as a sample would write it) |
|---|---|---|
| 1 | RETURN | Headwind and payload cut endurance, and 6 km with 20 min left leaves too little reserve. |
| 2 | RETURN | Assuming about 12 m/s airspeed, a headwind leaves about 4 m/s over the ground, so the distance takes too long. |
| 3 | CONTINUE | Assumes the headwind helps on the return leg and the mission target is near. |
| 4 | RETURN | Standard 20-30% battery reserve rule is not met. |
| 5 | RETURN | Headwind uncertainty and payload make continuing unsafe. |

Simulated agreement: 4 of 5 for RETURN. Disagreement is small on the final label but large in the reasoning, because each sample assumes a different airspeed and wind direction. That is the uncertainty to fix.

**Step 2 - exemplar (written by Claude in place of a human)**
```
Q: A drone with 20 min battery, 1 kg payload, 6 km from base and an 8 m/s headwind: continue or return?
Reasoning: The prompt has no airspeed or wind direction, so use the worst case. Assume cruise airspeed 12 m/s (illustrative). If the headwind is on the way home, ground speed is 12 - 8 = 4 m/s, so 6000 m / 4 = 1500 s = 25 min, which is more than the 20 min battery, and the payload increases power draw. If the headwind is on the way out, the return has a tailwind: 6000 / 20 = 300 s = 5 min, plenty of margin. Continuing means flying further away, which increases the return distance. Rule: if the energy needed to get home with a 25% reserve cannot be shown to be available under the worst-case wind, return now.
A: RETURN (now, and land early if the battery cannot cover the trip home)
```
**Step 3 - simulated re-run with exemplar:** with the worst-case rule shown, all 5 samples would be expected to say RETURN and to give the same energy-reserve reasoning (projected 5/5, not measured).

## Case 2: Irrigation (skip watering?)
Approx. words (prompt + output): about 360

**Step 1 - simulated 5 samples**
Question: Skip watering if 3 mm rain is forecast but soil is at 12%?
Where answers would vary: whether 3 mm of rain is enough to matter (it is small), whether the forecast is reliable, and whether 12% is critically dry for this soil (no soil type given).

| # | Answer | Reason |
|---|---|---|
| 1 | Do not skip | 12% is very dry and 3 mm is a small amount. |
| 2 | Skip | Rain is coming, so avoid over-watering; check again tomorrow. |
| 3 | Do not skip | Forecast rain is uncertain and light rain gets caught by leaves. |
| 4 | Skip | Assumes rain will arrive soon and the crop can wait a few hours. |
| 5 | Do not skip | Soil is far below the typical 25-30% threshold, so water a reduced amount. |

Simulated agreement: 3 vs 2, the largest disagreement among the three questions in this exercise, so it is the best candidate for an exemplar.

**Step 2 - exemplar (written by Claude)**
```
Q: Skip watering if 3 mm rain is forecast but soil is at 12%?
Reasoning: 3 mm on 1 m² is 3 L, a small amount compared with a typical daily crop demand of 4-6 mm. Soil at 12% is far below the usual 25-30% threshold, so the deficit is large and is not closed by 3 mm. The forecast may not arrive or may be intercepted by the canopy. So do not skip; water for the deficit minus the forecast rain (about 3 mm credit), and re-check soil moisture after the rain.
A: DO NOT SKIP - water a reduced dose (deficit minus 3 mm)
```
**Step 3 - simulated re-run:** projected 5/5 "do not skip, reduced dose". Not measured.

## Case 3: Path planning (replan or continue?)
Approx. words (prompt + output): about 340

**Step 1 - simulated 5 samples**
Question: Replan or continue when a new obstacle appears 1 cell ahead?
Where answers would vary: whether the obstacle is static or moving, and whether "replan" means a full replan or a local repair.

| # | Answer | Reason |
|---|---|---|
| 1 | REPLAN | An obstacle directly ahead blocks the current path. |
| 2 | REPLAN | Stop and replan locally to avoid a collision. |
| 3 | REPLAN | The stored path is now invalid. |
| 4 | CONTINUE | Assumes the obstacle is moving and will clear the cell. |
| 5 | REPLAN | Use incremental repair (D* Lite). |

Simulated agreement: 4 of 5 REPLAN; the variation comes from the unstated static-versus-moving assumption.

**Step 2 - exemplar (written by Claude)**
```
Q: Replan or continue when a new obstacle appears 1 cell ahead?
Reasoning: With one cell of clearance the robot cannot wait for a prediction. If the next cell is occupied, continuing along the current path causes a collision, whether the obstacle is static or moving, so first stop (or hold). Then check the path: if the cell is blocked, the current path is invalid. Repair it with incremental search (D* Lite) and resume. If the obstacle is known to be moving away, waiting a step is acceptable, but stopping is always safe.
A: STOP, then REPLAN (incremental repair)
```
**Step 3 - simulated re-run:** projected 5/5 "stop then replan". Not measured.

## Summary of this simulation
Most uncertain: irrigation (3:2), then drone (4:1 label, divergent reasoning), then path planning (4:1). The exemplar mainly works by making the missing assumption explicit (worst-case wind, soil deficit versus rain, stopping first). Cost: exemplars add roughly 100-150 words of prompt each.
