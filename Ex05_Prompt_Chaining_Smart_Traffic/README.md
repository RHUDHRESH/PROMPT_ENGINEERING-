# Ex-5: Comparing Prompting Techniques Through Engineering Problem-Solving (Prompt Chaining)

**Due:** 30 Aug 2026 · **Reference repo:** RaajaThilahar/Ex.No.5

## Project: AI-based Smart Traffic System
Chain: Problem -> Requirement Analysis -> Architecture -> Algorithm -> Flowchart -> Python Code -> Testing -> Documentation

Each step's output is pasted into the next prompt (marked `{{previous_output}}`).

| Step | Prompt | Output goes to |
|---|---|---|
| 1 | `prompts/1_problem.md` | `outputs/1_problem.md` |
| 2 | `prompts/2_requirements.md` | `outputs/2_requirements.md` |
| 3 | `prompts/3_architecture.md` | `outputs/3_architecture.md` |
| 4 | `prompts/4_algorithm.md` | `outputs/4_algorithm.md` |
| 5 | `prompts/5_flowchart.md` | `outputs/5_flowchart.md` |
| 6 | `prompts/6_code.md` | `src/traffic_controller.py` |
| 7 | `prompts/7_testing.md` | `tests/test_traffic_controller.py` |
| 8 | `prompts/8_documentation.md` | `outputs/8_documentation.md` |

A working reference implementation is already in `src/` and `tests/`. Run: `python -m unittest discover -s tests` from this folder.
`comparison.md` compares chained vs single-shot prompting.
