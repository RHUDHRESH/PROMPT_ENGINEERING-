# Evaluation

Score 1–5. ChatGPT was not run, so its rows are 'n/a - not run'. Claude scores are self-assessed by the model that produced the outputs (word counts checked by script) and are therefore biased.

| Level | Tool | Faithful to source | Follows constraints | Format correct | Readability | Notes |
|---|---|---|---|---|---|---|
| 1 Basic | ChatGPT | n/a - not run | n/a - not run | n/a - not run | n/a - not run | n/a - not run |
| 1 Basic | Claude | 4 | 5 | n/a (no format requested) | 4 | 102 words; faithful and includes model names GPT/Claude/Gemini. Jargon (self-attention, RAG) not explained; not tailored to students. |
| 2 Role | ChatGPT | n/a - not run | n/a - not run | n/a - not run | n/a - not run | n/a - not run |
| 2 Role | Claude | 4 | 5 | n/a (no format requested) | 4 | 123 words; adds a headline and paragraphs, slightly more magazine-like. Still no jargon explanations, and slightly longer than L1. |
| 3 Context | ChatGPT | n/a - not run | n/a - not run | n/a - not run | n/a - not run | n/a - not run |
| 3 Context | Claude | 4 | 5 | n/a (no format requested) | 5 | 131 words; explains tokens, hallucination and RAG in plain language, suited to students. Longest output; no length limit yet, so this is not a violation. |
| 4 Constraint | ChatGPT | n/a - not run | n/a - not run | n/a - not run | n/a - not run | n/a - not run |
| 4 Constraint | Claude | 4 | 4 | n/a (text) | 3 | 57 words (counted by script), under the 60 limit; no company names; jargon glossed in 3 words. Dense and telegraphic, hurting readability. Minor risk: 'human feedback', 'retrieval' are not glossed, and gloss of 'self-attention' is my own paraphrase. |
| 5 Format | ChatGPT | n/a - not run | n/a - not run | n/a - not run | n/a - not run | n/a - not run |
| 5 Format | Claude | 4 | 5 | 5 | 3 | JSON validated with json.load; headline 7 words, summary 52 words, all meanings <=3 words after one fix (one meaning first had 4 words and was corrected before saving). Exactly 2 limitations. No company names. Machine-readable but terse. |

## Observations
- **What changed most between levels?** Level 3 (context) changed the content most: the text gained plain-language explanations of tokens, hallucination and retrieval for the student audience. Level 4 (constraints) changed length and style most: from about 130 words down to 57, at the cost of readability. Level 2 (role) changed little beyond adding a headline and a magazine feel. Level 5 changed structure: valid, machine-readable JSON with glossed key terms.
- **Which constraint was ignored, and by which tool?** No constraint was ignored by Claude in this run: level 4 was 57 words, no company names, and glosses of 3 words or fewer; level 5 was valid JSON within the field limits. One draft glossary entry at level 5 was 4 words and was fixed before saving. Not all jargon in level 4 was glossed (for example 'fine-tuned', 'retrieval'), which is a soft weakness. For ChatGPT: not run, so nothing can be said.
- **Caveat:** levels 1-3 have no length limit, so their outputs are long relative to a sidebar; the comparison across levels is from a single run each and not repeated.
- **Final "user-defined" prompt chosen and why:** Level 5 as written, with one tweak for real use: add "Write the summary in plain sentences rather than telegraphic fragments, and gloss every technical term used in the summary." Level 5 is chosen because it is the only level whose output is verifiable (word counts, JSON validity), it keeps the audience context that made level 3 readable, and its constraints held. Its weakness, terse prose, is what the tweak addresses. Untested with ChatGPT.
