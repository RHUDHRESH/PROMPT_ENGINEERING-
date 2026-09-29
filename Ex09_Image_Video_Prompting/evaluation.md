# Evaluation

Tools: built-in Codex image generation for the image samples; Grok Imagine in the browser for one video sample. Image model version and seeds were not exposed. Scores are one-reviewer judgments; output variation is not measured statistically.

| Medium | Level | Output | Quality | Prompt adherence | Coherence | Style match | Observation |
|---|---|---|---:|---:|---:|---:|---|
| Image | 1 Simple | `generated_images/level1_imagegen.png` | 4 | 3 | 4 | N/A | Main subject and watering action are clear; the model added text/signage that the prompt did not request. |
| Image | 2 Detailed | `generated_images/level2_imagegen.png` | 5 | 5 | 5 | 4 | Brass robot, tomato plants, watering can and greenhouse are explicit and visible; warm light supports the requested setting. |
| Image | 3 Style + camera | `generated_images/level3_imagegen.png` | 5 | 5 | 5 | 5 | Cinematic lighting, shallow depth of field and left/right composition are clear. |
| Image | 4 Structured | `generated_images/level4_imagegen.png` | 4 | 5 | 4 | 3 | Subject and composition follow the fields, but the requested storybook watercolor reads closer to a realistic painterly image. |
| Video | 1 Simple | Grok Imagine, 6s at 480p; result remains in the signed-in Grok library | 3 | 3 | 3 | N/A | One browser sample generated for “A robot watering plants.” A visible frame showed a watering can and robot arm over a garden, but no full robot body; the 6-second player was available. The browser download remained incomplete, so no MP4 is included in the repository. Further generations were gated behind a ₹2,900/month plan; no subscription was started. |
| Video | 2–4 | Not generated | Not run | Not run | Not run | Not run | Grok required a paid subscription after the first sample. The free Hugging Face demos checked were unavailable (app did not respond or showed a runtime error). |

## Scoring rubric
- Quality: visual clarity and artefacts (5 = strong).
- Prompt adherence: requested elements visibly present (5 = all major elements).
- Coherence: plausible anatomy and scene (5 = consistent).
- Style match: fit to requested style (5 = close). N/A when no style was specified.

## Conclusion
For this four-image sample, adding subject details and action produced the clearest improvement over the short prompt. The camera and composition terms in level 3 were followed well. The structured style label was less reliable: the output looked more photographic than watercolor. One sample per prompt cannot separate prompt effects from random variation. One six-second Grok video was generated and reviewed in the browser. Levels 2–4 remain unrun because the service gated further generations behind a paid subscription and the free demos checked were unavailable. No video binary could be saved to this repository.
