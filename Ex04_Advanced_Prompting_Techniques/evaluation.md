# Evaluation

Score Reasoning and Correctness 1–5; Tokens = input+output (or words).

| Technique | Case | Tool | Reasoning | Correctness | Tokens | Notes |
|---|---|---|---|---|---|---|
| Zero-shot | Irrigation | | | | | |
| Few-shot | Irrigation | | | | | |
| CoT | Irrigation | | | | | |
| Persona | Irrigation | | | | | |
| Reverse | Irrigation | | | | | |
| Graph | Irrigation | | | | | |
| Active | Irrigation | | | | | |
| (repeat for Drone, Robot) | | | | | | |

## Ground truths to check against
- CoT irrigation: 2000 m² x 4 mm = 8000 L; minus 1 mm rain (2000 L) = 6000 L; 6000/30 = **200 min**.
- CoT drone: distance = 6x0.5 (delay) + 6²/(2x4) = 3 + 4.5 = **7.5 m < 30 m -> stops in time**. (Stop time 1.5 s of braking; the "2.5 s" in the prompt is a distractor — note if the model gets confused.)
- Dijkstra A->F: A-C(2)-B(3)-D(8)-E(10)-F(13) = **13** (path A,C,B,D,E,F).

## Conclusion
Best technique per case and token trade-off:
