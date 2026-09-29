# Comparison: ChatGPT vs Claude (identical prompts)

Score 1 (poor) – 5 (excellent). Add evidence in the notes column.

> Honesty note: ChatGPT was **not run**, so no head-to-head comparison exists yet. The Claude column is a **self-assessment** by the model that wrote the answers (not independent, so likely biased upward). Fill in the ChatGPT column after pasting its answers into `outputs/chatgpt.md`.

| Criterion | What to check | ChatGPT | Claude | Notes |
|---|---|---|---|---|
| Accuracy | Facts, formulas (attention formula correct?) | n/a - not run | 4 | Attention formula softmax(QKᵀ/√d_k)V given correctly; worked example (weights about 0.67/0.33) checks out by hand. Some figures (Chinchilla ~20 tokens/parameter) are given as approximate. |
| Creativity | Analogies, structure, examples | n/a - not run | 3 | Structured, with a query/key/value "looking for / offer / carry" framing and a small numeric example, but the answers are deliberately plain and not very inventive. |
| Hallucination | Fake papers/numbers? (5 = none) | n/a - not run | 4 | Only well-known papers cited (Vaswani 2017, Kaplan 2020, Hoffmann 2022, InstructGPT). The Wei et al. 2022 emergence paper was flagged as "unsure of exact title". Cost and energy figures were stated as uncertain. Not externally fact-checked, so not a 5. |
| Reasoning | Logical flow, why-not-just-what | n/a - not run | 4 | Explains why transformers beat RNNs (parallelism, path length, gradients) and notes trade-offs such as quadratic attention cost and Chinchilla vs inference-cost practice. |
| Speed | Seconds to complete (fill from outputs) | n/a - not run | not measured | No stopwatch timing was taken, so no speed number or score is given. |
| Engineering usefulness | Could you build/decide from it? | n/a - not run | 4 | Q3 table plus selection advice and Q5 stage/tool table are actionable. They stay high-level, with no code or hyperparameters. |
| **Total /30** | | n/a - not run | 19 of 25 scored (speed excluded) | Self-assessed and not comparable to a /30 total until Speed is measured. |

## Hallucination log
| Tool | Prompt | Claim | Verified? (source) |
|---|---|---|---|
| Claude | Q4 | Kaplan et al. 2020 "Scaling Laws for Neural Language Models" | Not re-verified in this session; well-known paper (arXiv 2001.08361) recalled from memory. Check before submission. |
| Claude | Q4 | Hoffmann et al. 2022 "Training Compute-Optimal Large Language Models" (Chinchilla), about 20 tokens per parameter | Not re-verified in this session; recalled from memory (arXiv 2203.15556). The 20:1 ratio is an approximation. |
| Claude | Q4 | Wei et al. 2022 emergent abilities paper | Marked "unsure of exact title" in the answer. Unverified. |
| Claude | Q4/Q5 | "Tens of millions of dollars" frontier training cost; InstructGPT used reward model plus PPO | Cost is an estimate flagged as uncertain. The PPO claim is from memory of Ouyang et al. 2022. Unverified here. |
| ChatGPT | all | n/a - not run | n/a - not run |

## Conclusion
No conclusion about which tool is better can be drawn, because ChatGPT was not run. On the Claude side alone, the answers were accurate as far as self-review can tell, respected the word limits, and flagged uncertainty instead of guessing. Run ChatGPT on the same five prompts, time both, and check the citations above before finalising scores.
