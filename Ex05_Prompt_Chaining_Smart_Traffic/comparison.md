# Prompt chain vs single-shot

**Honesty note.** The chain column reflects what was actually produced in this folder (outputs/1..8, `src/`, `tests/`). The single-shot column is NOT measured: no single-shot run was performed. It is my reasoned expectation of what a prompt like "build a smart traffic system" would typically give. Token/effort figures were not measured for either column.

| Aspect | Single prompt ("build a smart traffic system") - EXPECTED, not measured | Prompt chain (8 steps) - observed |
|---|---|---|
| Completeness | Likely a code sketch plus a short description; requirements, flowchart and test gaps probably thin or missing | All eight artefacts exist, plus a list of 16 uncovered edge cases |
| Consistency between artefacts | Fewer artefacts to conflict, but the design is implicit and unstated priorities may drift | The emergency > starved > longest-queue rule and parameters carry from requirements to algorithm, flowchart, code and docs. The flowchart omits the negative-queue check in green_time, a small gap |
| Code correctness (tests pass?) | Unknown; would need to be run | The reference code passes its 6 unit tests. The tests are shallow: many edge cases (notes in 7_testing_notes.md) are unchecked and some validation gaps exist in the code |
| Effort / total tokens | Expected lower: one prompt, one response | Not measured; clearly more (8 prompts, each carrying earlier output). Note that here the chain outputs were written after the code, so they are partly retro-fitted to it |
| Ease of fixing one stage | Harder: change means re-prompting everything | Easier: edit one stage and re-run downstream steps |

Conclusion: Chaining gives traceable, reviewable artefacts and a natural place to spot gaps (for example, the missing validation surfaced while writing step 7). Its cost is more effort. It does not by itself guarantee correctness; the tests do that. Since the single-shot numbers are unmeasured expectations, this comparison is qualitative only. A fair test would run both and count requirements covered and tests passed.
