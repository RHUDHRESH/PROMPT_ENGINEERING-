# Level 5 — Output format
```
You are a technical editor for an engineering magazine.
Context: the readers are final-year students who know basic ML but have not studied transformers. The summary will appear as a sidebar next to a longer article on LLMs.
Constraints: max 60 words in the summary; neutral tone; explain jargon in <=3 words; no company names; no facts outside the text.
Output format (JSON only):
{
  "headline": "<=8 words",
  "summary": "<=60 words",
  "key_terms": [{"term": "", "meaning": ""}],
  "limitations": ["", ""]
}
Summarize this text.

<paste source_text.md>
```
