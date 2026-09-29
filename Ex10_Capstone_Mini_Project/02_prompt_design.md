# Prompt design
Architecture: **System prompt** (role, safety) + **Context block** (farm data) + **Task prompt** + **Output schema**.
All prompts are stored in `prompt_repository/`:
| File | Role |
|---|---|
| `system.md` | Persona, safety rules, refusal policy |
| `irrigation.md` | Irrigation scheduling |
| `pest_diagnosis.md` | Symptom-based pest/disease triage |
| `fertiliser_plan.md` | Nutrient plan |

Techniques used: persona, few-shot, chain-of-thought (hidden reasoning, brief rationale shown), JSON output, clarifying-question fallback.
