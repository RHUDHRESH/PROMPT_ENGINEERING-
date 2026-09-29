# Comparison: ChatGPT and Claude on identical prompts

Scores use 1 (poor) to 5 (strong). The ChatGPT response is from the current Codex session; the Claude responses were already present in the repository. These were not timed, freshly launched side-by-side runs. The quality scores are provisional desk reviews, not independent human ratings.

| Criterion | What was checked | ChatGPT | Claude | Notes |
|---|---|---:|---:|---|
| Accuracy | Definitions, attention formula, scaling claims | 4 | 4 | Both give the standard attention equation and distinguish architecture families. The Claude answer's claims have not been independently checked; the ChatGPT report cites primary scaling papers but still needs faculty review. |
| Creativity | Analogies, examples, presentation | 3 | 3 | Both are structured and readable, with conventional examples rather than unusual analogies. |
| Hallucination control | Unsupported details and uncertainty | 4 | 4 | Both avoid precise undisclosed cost claims. The Claude response flags uncertainty. ChatGPT gives cautious general claims; paper titles and dates were checked against the linked primary papers in `report.md`. |
| Reasoning | Explanations and trade-offs | 4 | 4 | Both explain architecture choices and scaling trade-offs. |
| Speed | Completion seconds | Not measured | Not measured | No stopwatch was used. |
| Engineering usefulness | Can a student use it to choose or build? | 4 | 4 | Both provide architecture comparisons and an end-to-end build outline; neither gives implementation code or cost estimates. |
| **Total /25 scored** | Speed omitted because it was not measured | **19/25** | **19/25** | Provisional desk-review scores; a tie here does not establish equal quality across tasks. |

## Hallucination and verification log
| Tool | Claim | Check |
|---|---|---|
| Claude | Kaplan et al. (2020), *Scaling Laws for Neural Language Models* | Title and paper identifier are confirmed in `report.md` references. |
| Claude | Hoffmann et al. (2022), *Training Compute-Optimal Large Language Models* | Title and paper identifier are confirmed. The 20:1 token-to-parameter rule is an approximate summary, not a universal law. |
| Claude | Wei et al. (2022) emergent abilities paper | The repository output says it was unsure of the exact title. Do not cite that claim without checking the paper. |
| ChatGPT | Kaplan and Hoffmann scaling papers | Titles and identifiers were checked against arXiv records linked in `report.md`. |
| Both | Product-specific model architecture claims | Commercial implementation details may be undisclosed; treat examples as broad categories rather than verified internals. |

## Conclusion
Both answers cover the requested topics and offer useful introductory structure. The available records do not support a reliable speed ranking, and the Claude column was self-assessed in the original repository. Use the score table as a provisional exercise result; a fairer comparison would have a human reviewer score fresh answers from both tools without seeing their model labels.
