# Problem statement
Smallholder farmers lack timely, local, actionable agronomic advice. Extension officers are scarce, and generic chatbot answers ignore soil, crop stage, weather and budget.

**Goal:** an LLM-based advisor that turns farm inputs (crop, stage, soil moisture, forecast, budget) into a safe, prioritised action plan.

| Item | Definition |
|---|---|
| Users | Small farmers (1–5 ha), extension officers |
| Inputs | Crop, growth stage, soil test, 5-day forecast, budget, language |
| Outputs | Irrigation, fertiliser, pest advice, risk flags |
| Success metrics | ≥90% factual correctness on 30 test cases; 0 unsafe pesticide doses; response < 10 s |
| Out of scope | Legal/financial advice, banned chemicals |
