# Prompt types explained

| Type | Idea | When it shines | Risk |
|---|---|---|---|
| Straightforward | One clear instruction, no scaffolding | Simple, well-known tasks | Vague output if the task is ambiguous |
| Tabular format | Force rows/columns for input or output | Comparisons, checklists, structured data | Model may pad cells or break the table |
| Missing word | Give a template with blanks to fill | Controlling wording/tone, templates, quizzes | Model may rewrite the template |
| Preceding question | First question(s) build context, then the real ask | Multi-step reasoning, ambiguous user requests | Longer, more turns |

## Chatbot examples
- **Straightforward:** "A customer says their router keeps disconnecting. Give troubleshooting steps."
- **Tabular:** "Table: Symptom | Likely cause | Fix | Escalate? for 5 router issues."
- **Missing word:** "Hi ___, your order ___ is currently ___ and should arrive by ___."
- **Preceding question:** "Q1: What info do you need to track an order? Q2: What if the ID is invalid? Now answer: 'Where is my order?'"
