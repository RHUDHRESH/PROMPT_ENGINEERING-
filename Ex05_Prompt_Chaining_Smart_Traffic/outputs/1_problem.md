# Step 1 - Problem statement

*Produced by running `prompts/1_problem.md` (answer written by Claude, in-session).*

**Context.** A 4-way urban intersection (approaches N, E, S, W) is controlled by fixed-time signals. The fixed cycle ignores actual demand, so green time is wasted on empty approaches while other queues grow.

**Current issues**
- Fixed green splits do not track queue length, especially at peaks.
- Emergency vehicles are delayed by ordinary queues.
- A very busy approach can dominate a naive "longest queue" policy and leave a small approach waiting indefinitely.
- No central visibility of waiting times or throughput.

**Stakeholders:** drivers and pedestrians, emergency services, city traffic authority, maintenance staff, urban planners.

**Goals:** allocate green time in proportion to demand within safe bounds; give emergency vehicles immediate priority; guarantee no approach with waiting vehicles is starved.

**Measurable success metrics**
| Metric | Target (vs fixed-time baseline) |
|---|---|
| Average wait time per vehicle | reduced by at least 20% |
| Throughput (vehicles/hour) | increased by at least 10% |
| Emergency response delay at the junction | under 10 s from detection to green |
| Maximum consecutive skipped cycles for a non-empty approach | at most 3 |
