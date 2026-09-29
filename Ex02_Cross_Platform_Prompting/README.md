# Ex-2: Cross-Platform Prompting — Evaluating Diverse Prompt Engineering Techniques

**Due:** 10 Sep 2026 · **Reference repo:** RaajaThilahar/Ex.No.2

## Objective
Design prompts using different structures and show how one task improves from a basic prompt to a fully specified one.

## Chosen application: Text Summarization
Source text: `source_text.md` (same input for every prompt level).

## Prompt ladder
| Level | File | What it adds |
|---|---|---|
| 1 Basic | `prompts/1_basic.md` | Just the task |
| 2 Role | `prompts/2_role.md` | Who the model is |
| 3 Context | `prompts/3_context.md` | Audience and purpose |
| 4 Constraint | `prompts/4_constraint.md` | Length, tone, exclusions |
| 5 Output format | `prompts/5_output_format.md` | Exact structure |

## Procedure
Run each level on at least two platforms (e.g. ChatGPT, Claude), save the results in `outputs/level<N>_<tool>.md`, then complete `evaluation.md`.
