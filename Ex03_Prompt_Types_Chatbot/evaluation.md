# Evaluation (score 1-5)

**Important:** only the Claude rows were run and scored. ChatGPT was not run for this exercise, so those rows are marked "n/a - not run". Claude scores are a self-assessment by the model that wrote the outputs (so likely lenient); they should be re-scored by a human reviewer. Reply word counts were checked mechanically for the length limits.

| Prompt type | Tool | Relevance | Tone/UX | Structure followed | Accuracy | Notes |
|---|---|---|---|---|---|---|
| Straightforward | ChatGPT | n/a - not run | n/a - not run | n/a - not run | n/a - not run | n/a - not run |
| Straightforward | Claude | 5 | 5 | 5 | 4 | Both prompts answered. Headphone reply about 100 words (limit 120). Order reply stated the no-database limitation honestly and gave tracking routes. Accuracy 4 because generic steps (pairing button, "3 business days") are typical, not product-specific. |
| Tabular | ChatGPT | n/a - not run | n/a - not run | n/a - not run | n/a - not run | n/a - not run |
| Tabular | Claude | 5 | 4 | 5 | 4 | 6 rows in the requested 2/2/2 split, correct 4 columns, all bot replies 18-23 words (limit 25). Tone is terse because of the word cap. Escalation flags (burning smell, lost parcel = Y) are sensible. Policy answers are deliberately generic. |
| Missing word | ChatGPT | n/a - not run | n/a - not run | n/a - not run | n/a - not run | n/a - not run |
| Missing word | Claude | 5 | 4 | 5 | 4 | All 7 blanks filled, sentence skeleton unchanged, only completed text returned. The two "first/if that doesn't work" blanks became long clauses, which stretches the sentence. Brand ("SmartKettle") and "one business day" were inferred/assumed. |
| Preceding question | ChatGPT | n/a - not run | n/a - not run | n/a - not run | n/a - not run | n/a - not run |
| Preceding question | Claude | 5 | 5 | 5 | 4 | Q1-Q3 answered briefly, and the final reply visibly uses them (info request, likely causes, apologetic and action-oriented tone). Longest output of the four types. Does not promise specifics it cannot know. |

## Conclusion
For a customer-support chatbot, no single type wins everywhere, but the ranking from this run is:

1. **Preceding-question prompting** gave the best customer-facing reply for an emotional, ambiguous case (late order). Forcing the model to decide what information is needed, the likely causes and the right tone first produced a reply that apologised, asked for exactly the right details and set expectations. Cost: more output text and turns, so it suits hard or sensitive tickets rather than every message.
2. **Straightforward prompting** is the best default for simple, well-known problems (headphone pairing, tracking help). It is short and cheap, and worked well when the prompt carried role, tone and length limits. It is weakest when the request is ambiguous.
3. **Tabular prompting** is best for design and review work (planning intents, replies and escalation rules in one view, auditing consistency), not for live conversation. The word cap made replies flat.
4. **Missing-word prompting** gives the tightest control over wording and is ideal for templated messages (order updates, apology emails). The skeleton constrains the model, so replies can be awkward when a blank needs a long clause.

Recommended design: use a missing-word template for routine, high-volume messages, straightforward prompts for simple troubleshooting, and preceding-question prompting for complaints and escalations, with tabular prompts used offline to define intents and escalation rules. Caveat: this comparison covers one tool (Claude) with self-scoring; the cross-tool comparison the exercise asks for still needs the ChatGPT runs.
