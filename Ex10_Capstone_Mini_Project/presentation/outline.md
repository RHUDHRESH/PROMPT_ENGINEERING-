# Presentation: slide-by-slide speaker notes (10 slides, about 10 minutes)

Honesty note to keep visible on slides 7 and 10: results are Claude self-evaluated on a sample; no live deployment or independent grading yet.

## Slide 1 - Title and domain (0:30)
On slide: "Smart Agriculture Advisor: prompt engineering for smallholder farms", name, date.
Say: This project applies prompt engineering to agriculture. The goal is a safe, structured advisor for small farmers, built only with prompts, not model training.

## Slide 2 - The problem (1:00)
On slide: scarce extension officers; generic chatbot answers; risk of unsafe chemical advice.
Say: A farmer with 2 hectares needs advice that reflects their soil moisture, crop stage and forecast. Generic answers ignore this, and a wrong pesticide dose can harm people and water. That is why the prompts are constrained.

## Slide 3 - Users and metrics (0:45)
On slide: users; inputs; outputs; targets (90% correct on 30 cases, 0 unsafe doses, under 10 s).
Say: These are targets, not achievements. I will say later which ones I have actually checked.

## Slide 4 - Prompt architecture (1:15)
On slide: diagram: system prompt -> FARM DATA -> task prompt -> JSON schema.
Say: The system prompt sets the persona and five rules. The context block injects farm data. A task prompt selects irrigation, pest or fertiliser. The schema forces a JSON reply so an app can display it and a script can check it.

## Slide 5 - Prompt repository sample (1:00)
On slide: irrigation.md snippet with the tomato example.
Say: The example inside the prompt anchors the format. Variables like {{moisture}} make the prompts reusable across farms.

## Slide 6 - Iteration journey (1:00)
On slide: v1 to v5 table.
Say: Each version fixed one failure: generic advice, then verbosity, then safety, then parseability, then guessing. The scores are qualitative notes, not measurements.

## Slide 7 - Evaluation (1:30)
On slide: 30 scenarios in three groups; 10 answered; validator pass; caveat banner.
Say: I wrote 30 scenarios with conservative expected answers based on generic FAO-style agronomy. I answered ten myself as the model; all ten matched my key and passed the schema validator. I was both author and grader, so this shows the design works, not that we hit 90%. Next step: an agronomist grades all 30 against a live model.

## Slide 8 - Demo (1:30)
On slide: screenshot placeholders for three cases.
Say: Follow demo/demo_script.md: an irrigation case, a missing-data case that triggers questions, and an unsafe dose request that is refused. Then run the validator.

## Slide 9 - Ethics and limits (0:45)
On slide: safety, hallucination, access, privacy, accountability, environment.
Say: The tool is decision support. It asks when unsure, states confidence, refuses banned or over-label chemicals, and should be reviewed by local experts. Local-language output needs native-speaker review.

## Slide 10 - Conclusion and future work (0:45)
On slide: done vs not done; next steps.
Say: Done: prompt repository, test set, validator, sample outputs, ethics. Not done: live deployment, measured accuracy and latency, expert grading, farmer testing. Next: retrieval from local extension documents, weather and sensor inputs, voice in local languages. Thank you; questions.

## Anticipated questions
- Why JSON? Machine-readable output and automatic validation.
- Does the validator prove the advice is right? No, it checks structure only.
- Why not fine-tune? Prompts are cheap to iterate and inspect; fine-tuning could be a later step.
