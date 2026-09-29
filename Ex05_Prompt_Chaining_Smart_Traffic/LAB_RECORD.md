# Lab Record: Ex-5: Prompting Through Engineering Problem-Solving

| Field | Entry |
|---|---|
| Name / Reg. No. | ______________ |
| Date | ______________ |
| Repo | https://github.com/RHUDHRESH/PROMPT_ENGINEERING- |

## Aim
Solve an engineering problem via a prompt chain (problem to documentation).

## Tools / Apparatus
Claude-generated chain artefacts and Python reference implementation; 6 Python unit tests passed in this session

## Procedure
1. Prompts written (see `prompts/` or the folder README).
2. Each prompt run on every tool; raw outputs saved under `outputs/` (or the folder's equivalent).
3. Results scored in `comparison.md` on: Consistency, code correctness, effort.
4. Findings summarised below.

## Observations
See `comparison.md`. Add your own scores for any tool you ran yourself. Tools not run are left blank; do not fill them in from memory.

## Result
An eight-step prompt chain links requirements through documentation for a smart traffic controller. The reference code passes six Python unit tests. The single-shot comparison is an unmeasured expectation, not an experimental result.

## Conclusion
Chaining makes intermediate requirements reviewable and gives a clear place to find drift. Tests still determine code behaviour; the chain does not guarantee correctness. Broader edge cases and a measured single-shot baseline would strengthen the study.

## Faculty signature: ______________
