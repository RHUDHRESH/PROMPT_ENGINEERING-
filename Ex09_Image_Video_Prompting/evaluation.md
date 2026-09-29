# Evaluation

Tool: built-in image generation in Codex. Exact model version and seed were not exposed. One image was generated per prompt tier. Scores are one-reviewer judgments; output variation is not measured statistically.

| Medium | Level | Output | Quality | Prompt adherence | Coherence | Style match | Observation |
|---|---|---|---:|---:|---:|---:|---|
| Image | 1 Simple | `generated_images/level1_imagegen.png` | 4 | 3 | 4 | N/A | Main subject and watering action are clear; the model added text/signage that the prompt did not request. |
| Image | 2 Detailed | `generated_images/level2_imagegen.png` | 5 | 5 | 5 | 4 | Brass robot, tomato plants, watering can and greenhouse are explicit and visible; warm light supports the requested setting. |
| Image | 3 Style + camera | `generated_images/level3_imagegen.png` | 5 | 5 | 5 | 5 | Cinematic lighting, shallow depth of field and left/right composition are clear. |
| Image | 4 Structured | `generated_images/level4_imagegen.png` | 4 | 5 | 4 | 3 | Subject and composition follow the fields, but the requested storybook watercolor reads closer to a realistic painterly image. |
| Video | 1–4 | No video files | Not run | Not run | Not run | Not run | This session had no video generation tool. Prompts are prepared, but quality and temporal consistency cannot be scored honestly. |

## Scoring rubric
- Quality: visual clarity and artefacts (5 = strong).
- Prompt adherence: requested elements visibly present (5 = all major elements).
- Coherence: plausible anatomy and scene (5 = consistent).
- Style match: fit to requested style (5 = close). N/A when no style was specified.

## Conclusion
For this four-image sample, adding subject details and action produced the clearest improvement over the short prompt. The camera and composition terms in level 3 were followed well. The structured style label was less reliable: the output looked more photographic than watercolor. One sample per prompt cannot separate prompt effects from random variation. The video part remains unrun because a video model was unavailable in this session.
