# Evaluation

Scores use 1–5. ChatGPT outputs were produced in the current Codex session; Claude outputs were already in the repository. The ChatGPT scores are provisional review by the model that produced those outputs, while the repository's Claude scores were originally self-assessed. Word counts and JSON can be checked mechanically; readability scores are subjective. No stopwatch was used.

| Level | Tool | Faithful to source | Follows constraints | Format correct | Readability | Notes |
|---|---|---:|---:|---:|---:|---|
| 1 Basic | ChatGPT | 5 | 5 | N/A | 4 | Covers the source's main claims without a requested length cap; concise. |
| 1 Basic | Claude | 4 | 5 | N/A | 4 | Original repository score; covers the central points and names products. |
| 2 Role | ChatGPT | 5 | 5 | N/A | 5 | Adds a headline and magazine-style paragraphs without unsupported facts. |
| 2 Role | Claude | 4 | 5 | N/A | 4 | Original repository score; more magazine-like than level 1. |
| 3 Context | ChatGPT | 5 | 5 | N/A | 5 | Explains token, hallucination and retrieval in plain language for the stated audience. |
| 3 Context | Claude | 4 | 5 | N/A | 5 | Original repository score; explains several technical terms for students. |
| 4 Constraint | ChatGPT | 5 | 4 | N/A | 4 | 49-word reply and no company names. Some technical terms could be glossed more explicitly. |
| 4 Constraint | Claude | 4 | 4 | N/A | 3 | Original repository score; 57 words, but dense and not all jargon is glossed. |
| 5 Format | ChatGPT | 5 | 5 | 5 | 4 | JSON has the requested keys; headline is under 8 words, summary under 60 words, and limitations has two entries. |
| 5 Format | Claude | 4 | 5 | 5 | 3 | Original repository score; JSON was reported as validated, with terse wording. |

## Observations
- Context and constraints change the content and audience fit most; formatting makes the output machine-checkable.
- Level 4 is 49 words in the ChatGPT output and uses no company names. Its explanations can still improve.
- Level 5 follows the requested structure. The fenced payload should be passed to `json.loads` if machine validation is required.
- The saved outputs are single samples; fresh identical runs and blind human scoring would make this comparison more reliable.

## Final user-defined prompt
Level 5, with this added instruction: “Write the summary in plain sentences rather than fragments, explain every technical term used, and include only facts stated in the source.” It keeps audience context and produces verifiable fields while addressing the terse style seen in the saved samples.
