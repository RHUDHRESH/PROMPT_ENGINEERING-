# Active prompting (uncertainty-driven example selection)
Procedure: run the question 5 times, find the question with the most disagreement among answers, then have a human write a chain-of-thought exemplar for it and add it as a few-shot example.

**Step 1 – sample (run 5x)**
```
Should a drone with 20 min battery, carrying a 1 kg payload, 6 km from base and facing 8 m/s headwind, continue the mission or return? Answer CONTINUE or RETURN and give a one-line reason.
```
**Step 2 – exemplar (human-written)**
```
Q: <the most uncertain question>
Reasoning: <your step-by-step reasoning>
A: <correct answer>
```
**Step 3 – re-run with the exemplar prepended** and compare consistency across 5 runs.
Repeat for irrigation ("Skip watering if 3 mm rain is forecast but soil is at 12%?") and path planning ("Replan or continue when a new obstacle appears 1 cell ahead?").
