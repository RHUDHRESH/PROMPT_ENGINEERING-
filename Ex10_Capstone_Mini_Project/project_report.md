# Smart Agriculture Advisor - Project Report

## 1. Abstract
Smallholder farmers often lack timely, local agronomic advice because extension officers are scarce. This project designs a prompt-engineered large language model (LLM) assistant, "AgriAdvisor", that turns structured farm data (crop, growth stage, soil moisture, forecast, soil test, budget, language) into a safe, prioritised action plan in a fixed JSON format. The work covers problem definition, a reusable prompt repository (system prompt plus irrigation, pest diagnosis and fertiliser task prompts), an iteration log, a 30-scenario test set with conservative expected answers, thirty model replies written and self-evaluated by Claude, a small Python validator for the JSON schema, and an ethics analysis. **Important limitation:** no deployed system, user study, latency measurement or independent grading was performed. The reported results are self-evaluation of Claude's own replies against a key Claude also wrote and must not be read as measured performance.

## 2. Problem Statement
Generic chatbot answers ignore soil, crop stage, weather and budget, and can suggest unsafe chemical use. The goal is an advisor that (a) uses only the data supplied, (b) asks clarifying questions when critical data is missing, (c) prefers low-cost, low-chemical options, (d) states confidence and assumptions, and (e) never exceeds label doses or recommends banned products. Users are farmers with 1-5 ha and extension officers. Target metrics, defined in `01_problem_statement.md`: at least 90% factual correctness on 30 test cases, zero unsafe pesticide doses, and response time under 10 seconds. Out of scope: legal and financial advice, and banned chemicals.

## 3. Prompt Design
The architecture (see `02_prompt_design.md`) has four layers: a **system prompt** (role, five rules, output schema), a **context block** (FARM DATA with template variables such as `{{crop}}` and `{{moisture}}`), a **task prompt** (irrigation, pest diagnosis, or fertiliser plan), and an **output schema** (JSON with `summary`, `actions[priority, action, why, cost]`, `risks`, `confidence`, `questions`).

Techniques used:
- Persona and rules (system prompt) to constrain behaviour.
- Few-shot / worked example (the irrigation prompt includes an example case); few-shot prompting was described by Brown et al. (2020).
- Brief rationale rather than long reasoning shown to the farmer; step-by-step reasoning prompts are studied by Wei et al. (2022).
- Structured JSON output so an app can render the plan and so it can be checked automatically (`prompt_repository/validate_output.py`).
- Clarifying-question fallback: up to three questions when a critical field is missing.
- Safety rules: no banned or restricted pesticides, no doses beyond label guidance, refer to the extension officer for chemicals, consistent with the spirit of the FAO/WHO International Code of Conduct on Pesticide Management.
- Multilingual reply: the `{{language}}` variable sets the reply language while JSON keys stay in English.

## 4. Prompt Iteration
Five versions were logged (`03_prompt_iteration.md`): v1 a bare request ("Give farming advice for tomato"), v2 added a FARM DATA block, v3 added persona and safety rules, v4 added the JSON schema, v5 added the clarifying-question rule. The scores in that table are qualitative labels (generic, more specific, safer, consistent, fewer guesses) recorded by the author, not numeric measurements. The main lesson is that each addition targeted one observed failure: generic answers, verbosity, unsafe chemical suggestions, unparseable output, and guessing when data was missing. A further iteration, not yet done, should test the prompts on all 30 scenarios and adjust wording where replies fail the checks.

## 5. AI Output Evaluation
`04_output_evaluation.md` holds 30 scenarios: 10 irrigation, 10 fertiliser and 10 pest, disease and safety cases (including missing data, an out-of-scope request, a Hindi-language request, a request to double a pesticide dose, and a request for a banned product). Expected answers are deliberately conservative and follow generic, widely taught agronomy: irrigate at dawn for dry flowering tomato; skip irrigation before forecast rain; split nitrogen applications; lime acid soil according to a lab recommendation; delay urea before heavy rain; legumes need little nitrogen; scout and use integrated pest management first. The reference basis is named generically (FAO irrigation, plant nutrition and IPM guidance), and local extension advice always overrides.

All 30 scenarios were answered by Claude: 10 in `prompt_repository/sample_outputs.md` and 20 in `sample_outputs_part2.md`. Results, all **Claude self-evaluated**:
- All thirty replies matched the expected answer in the author's own judgement (author is also the grader, so this is not independent evidence).
- No unsafe dose advice appeared in the thirty replies; two safety scenarios (27, 28) were refused with safer alternatives.
- All thirty replies passed the schema validator (a unittest confirms this).
- Latency was not measured, and no independent grader (e.g. an agronomist) has reviewed the replies.

Because the same author wrote the expected answers and the replies and graded them, these results demonstrate that the format and rules work in principle, not that the 90% target is met. Independent grading by an agronomist over all 30 scenarios is required before any accuracy claim.

The validator checks: valid JSON (a code fence is tolerated), exact key set, priorities as unique integers in order, cost in {low, med, high}, confidence in {high, medium, low}, non-empty strings, and at most three questions.

## 6. Ethical Considerations
Summarised from `05_ethical_considerations.md`:
- **Safety:** wrong chemical or dose advice can harm people, crops and water. Hard rules, label-only dosing, and expert referral are built in.
- **Hallucination:** the advisor must ask when data is missing, show confidence, and state assumptions. LLMs can still be wrong, so outputs are decision support.
- **Bias and access:** language, literacy and connectivity limit who can benefit; a local-language, low-bandwidth mode is needed. Hindi output in the samples needs native-speaker review.
- **Privacy:** farm location and yield data are sensitive; minimise collection, encrypt, and obtain consent.
- **Accountability:** the advice does not replace agronomists, and users should be told so in the interface.
- **Environmental impact:** integrated pest management first and avoiding over-fertilisation reduce runoff and pollution.
- **Prompt injection and scope:** scenario 29 tests refusal of out-of-scope or rule-overriding requests.

## 7. Demonstration
`demo/demo_script.md` gives a step-by-step walkthrough using three scenarios (irrigation, pest triage with a follow-up question, and a refused unsafe request) and the validator. No screen recording or screenshots are included in the repository yet; they must be captured by running the demo.

## 8. Conclusion and Future Work
The project delivers a reusable, structured prompt repository, a test set with conservative expected answers, a checkable output schema, and sample replies with an honest self-evaluation. What has not been done: deploying the prompts against a live model, measuring accuracy, latency and cost, independent expert grading, and testing with real farmers. Future work: (1) run all 30 scenarios and record raw replies; (2) have an agronomist grade them; (3) add retrieval from vetted local extension documents so advice cites local guidance; (4) integrate weather and soil-sensor inputs; (5) add voice and local-language interfaces; (6) extend validation to semantic safety checks, such as flagging any numeric pesticide dose.

## 9. References
- Allen, R. G., Pereira, L. S., Raes, D., Smith, M. (1998). *Crop evapotranspiration: Guidelines for computing crop water requirements.* FAO Irrigation and Drainage Paper 56. Food and Agriculture Organization of the United Nations.
- Doorenbos, J., Kassam, A. H. (1979). *Yield response to water.* FAO Irrigation and Drainage Paper 33. FAO.
- FAO and WHO. *International Code of Conduct on Pesticide Management* (revised 2014).
- FAO. Guidance on integrated pest management and on fall armyworm management (FAO publications and website; check the current edition).
- Brown, T. B. et al. (2020). Language Models are Few-Shot Learners. *NeurIPS 33*.
- Wei, J. et al. (2022). Chain-of-Thought Prompting Elicits Reasoning in Large Language Models. *NeurIPS 35*.
- Course reference repository named in the README: RaajaThilahar/Ex.No.10.
