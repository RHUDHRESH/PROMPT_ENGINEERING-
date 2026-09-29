# Evaluation

Score Reasoning and Correctness 1-5. **Tool = Claude only** (ChatGPT/other tools were not run). Scores are a self-assessment by the model that wrote the outputs, so treat them as provisional and re-score by hand.

**Tokens column:** real token counts were not available. The figure is an **approximate word count** (prompt + output, prompt estimated at about 45 words), rounded to the nearest 10. It is a proxy only; actual tokens are usually about 1.3x the word count for English text.

Rows for Active prompting come from a **simulation** (5 samples reasoned, not run); see `outputs/active_claude.md`.

| Technique | Case | Tool | Reasoning | Correctness | Tokens (approx. words) | Notes |
|---|---|---|---|---|---|---|
| Zero-shot | Irrigation | Claude | 3 | 4 | ~230 | Reasonable pseudocode with tunable thresholds (illustrative values); no calibration. |
| Few-shot | Irrigation | Claude | 3 | 4 | ~110 | WATER (short); the label is a judgement between examples. Cheapest. |
| CoT | Irrigation | Claude | 5 | 5 | ~120 | 8000 - 2000 = 6000 L; 6000/30 = 200 min, matches ground truth. |
| Persona | Irrigation | Claude | 4 | 4 | ~290 | Practical and plain, budget-aware; numbers are rules of thumb. |
| Reverse | Irrigation | Claude | 4 | 5 | ~190 | Six well-targeted questions covering crop, water, soil, budget, power, goals. |
| Graph | Irrigation | Claude | 4 | 5 | ~270 | Adjacency list plus SPOF analysis (controller, pump/valve, sensor). |
| Active | Irrigation | Claude | 4 | 4 | ~360 | Simulated. Most uncertain of the three (3:2). Exemplar gives "do not skip, reduced dose". |
| Zero-shot | Drone | Claude | 3 | 4 | ~280 | Sound VIO/tracker/avoidance pipeline; notes monocular scale ambiguity. |
| Few-shot | Drone | Claude | 3 | 4 | ~120 | Yaw 30 deg right, slow, pass behind; action is a judgement, no single correct answer. |
| CoT | Drone | Claude | 5 | 5 | ~210 | 3 + 4.5 = 7.5 m < 30 m; flagged the prompt's 2.5 s as inconsistent and bounded it (15 m). |
| Persona | Drone | Claude | 5 | 4 | ~290 | Strong failure-mode list (spoofing, altitude error, dropout) and fixes. |
| Reverse | Drone | Claude | 4 | 4 | ~240 | Reconstructed prompt plus context list; inherently speculative. |
| Graph | Drone | Claude | 4 | 5 | ~260 | Mermaid state machine; no unreachable states, dead ends and a livelock loop identified. |
| Active | Drone | Claude | 4 | 4 | ~450 | Simulated. Exemplar makes wind/airspeed assumptions explicit; assumed 12 m/s airspeed is illustrative. Most tokens. |
| Zero-shot | Robot | Claude | 4 | 4 | ~170 | A* with Manhattan on 20x20 with justification. |
| Few-shot | Robot | Claude | 4 | 5 | ~90 | D* Lite; correct for known-but-changing grid. Cheapest. |
| CoT | Robot | Claude | 5 | 5 | ~320 | Included the tie-breaking caveat: with Manhattan and arbitrary ties, A* can still expand the whole rectangle. |
| Persona | Robot | Claude | 4 | 5 | ~260 | Correctly identifies BFS ignores weights; full-credit path Dijkstra/A*/D* Lite. |
| Reverse | Robot | Claude | 3 | 3 | ~240 | The "pasted design document" does not exist; used a stand-in (A* on 20x20) and said so. |
| Graph | Robot | Claude | 5 | 5 | ~310 | Full distance table; shortest path A,C,B,D,E,F = 13 (verified). |
| Active | Robot | Claude | 4 | 4 | ~350 | Simulated. Answer "stop then replan"; least disagreement (4:1) in simulation. |

## Ground truths to check against (verified)
- **CoT irrigation:** 2000 m² x 4 mm = 8000 L (1 mm over 1 m² = 1 L); minus 1 mm rain (2000 L) = 6000 L; 6000/30 = **200 min**. Verified correct.
- **CoT drone:** distance = 6 x 0.5 (delay) + 6²/(2x4) = 3 + 4.5 = **7.5 m < 30 m -> stops in time**. Verified correct. **Correction to the earlier note:** the old note called "2.5 s" a distractor and said stop time was 1.5 s of braking. The calculation is right (braking time 6/4 = 1.5 s), but the prompt's "needs 2.5 s to stop" is not a harmless distractor: it is inconsistent with the other numbers, since 0.5 s delay + 1.5 s braking = **2.0 s** total, not 2.5 s. The answer does not depend on it: even at constant 6 m/s for the whole 2.5 s the drone covers at most 15 m (< 30 m). Good answers should use v²/(2a) and state the inconsistency. (If instead 2.5 s were the braking time alone, deceleration would be 6/2.5 = 2.4 m/s², not 4 m/s², so the prompt over-specifies.)
- **Dijkstra A->F:** verified. Distances: C=2, B=3 (via C), D=8 (via B), E=10 (via D), F=13 (via E); path A, C, B, D, E, F = **13**. The other candidate A, C, B, D, F = 14. The old note listed the path as "A-C(2)-B(3)-D(8)-E(10)-F(13)", where the numbers are cumulative distances (edge weights are 2, 1, 5, 2, 3); this is correct but easily misread as edge weights.

## Conclusion
**Best technique per case (from these outputs, self-assessed):**
- **Irrigation:** Chain-of-Thought for the calculation (exact, checkable, cheap at ~120 words). For design questions, Graph prompting gave the most useful structure (critical path and single points of failure), and Reverse prompting is the best first step when requirements are unknown.
- **Drone:** Chain-of-Thought for the stopping-distance question because it exposed the inconsistent 2.5 s figure; Persona (flight-controller engineer) for safety review; Graph (state machine) for mission-logic verification.
- **Robot:** Graph prompting with Dijkstra was exact and fully verifiable (13); CoT was best for the A* versus Dijkstra comparison, and Few-shot was the cheapest correct choice of algorithm (D* Lite, ~90 words).

**Token trade-off:** Few-shot (~90-120 words) and CoT numeric problems (~120) were the cheapest per useful answer. Persona, Graph and Reverse cost about 200-300 words and repay it when the task needs breadth, structure or review. Active prompting was the most expensive (350-450 words) because it involves 5 samples plus an exemplar plus a re-run, and here it was only simulated, so its benefit (more consistent answers) is unproven by this exercise. Overall rule: use CoT for calculations, Few-shot for classification or choices with clear precedents, Persona/Graph for design and safety analysis, Reverse for requirements gathering, and reserve Active prompting for places where repeated runs really do disagree.

**Caveats:** single tool, self-scored, word counts instead of tokens, and Active prompting simulated.
