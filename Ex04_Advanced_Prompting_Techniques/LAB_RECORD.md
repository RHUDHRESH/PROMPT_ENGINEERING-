# Lab Record: Exp-4: Advanced Prompt Engineering Techniques

| Field | Entry |
|---|---|
| Name / Reg. No. | ______________ |
| Date | ______________ |
| Repo | https://github.com/RHUDHRESH/PROMPT_ENGINEERING- |

## Aim
Implement zero-shot, few-shot, CoT, persona, reverse, graph and active prompting on engineering case studies.

## Tools / Apparatus
Claude outputs cover the seven techniques; Grok (Fast) browser runs cover the Active Prompting samples only. ChatGPT and other platform runs for the other techniques were not performed.

## Procedure
1. Prompts written (see `prompts/` or the folder README).
2. Claude outputs are under `outputs/`. Grok ran five independent baseline and five exemplar-guided samples for each Active Prompting case; see `outputs/active_grok.md`.
3. Results scored in `evaluation.md` on: Reasoning, correctness, token usage.
4. Findings summarised below.

## Observations
See `evaluation.md` and `outputs/active_grok.md`. Claude scores are self-assessments; Grok active-prompting results report observed decisions and are not expert scores.

## Result
Seven techniques were applied to irrigation, drone navigation and robot path planning. Checkable calculations and the Dijkstra graph answer were compared with hand-worked ground truths; token values are word-count proxies.

## Conclusion
Graph prompting made relationships and paths easy to inspect; few-shot prompts were concise for choices with clear examples. The Claude Active Prompting rows are simulations; separate Grok browser samples were run five times before and after a human-written exemplar for each case.

## Faculty signature: ______________
