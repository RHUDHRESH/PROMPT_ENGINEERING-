# Smart Agriculture Advisor — presentation outline

Nine-slide talk, about 8 minutes. The editable deck is `Smart_Agriculture_Advisor_v2.pptx`.

## Slide 1 — Smart Agriculture Advisor (0:30)
Introduce the prompt-engineering capstone and agriculture domain. The project is an educational prototype, not field-tested advice.

## Slide 2 — Problem statement (1:00)
Explain why crop stage, moisture, forecast, water access and local practice matter. Generic answers can be unsafe when context is missing.

## Slide 3 — Project scope (0:45)
Describe the three tasks: irrigation, pest triage and fertiliser planning. State that an agronomist and local label guidance remain authoritative.

## Slide 4 — Prompt design (1:00)
Show how the system prompt requests missing data, separates facts from assumptions, communicates uncertainty and avoids inventing chemical doses or measurements.

## Slide 5 — Prompt iteration (1:00)
Walk through the shift from a vague request to farm-specific fields, explicit uncertainty, and a structured response a person can review.

## Slide 6 — Output evaluation (1:00)
Explain checks for completeness, supplied facts, uncertainty, actionability and output shape. State that the sample outputs were self-evaluated by the model author and no agronomist has reviewed them. The validator checks format only.

## Slide 7 — Prototype workflow (0:45)
Trace farmer question → task prompt and farm details → model response → format validator → farmer or agronomist review. The prototype does not control farm equipment.

## Slide 8 — Ethical and practical limits (1:00)
Cover privacy, uncertain advice, local language/connectivity, chemical safety and human accountability.

## Slide 9 — Demonstration and next steps (1:00)
Use the demo script to show irrigation input, missing-data questions, a structured response and validator. Future work: independent agronomist review, repeated tests, farmer feedback and local-language support. No live model recording is included.
