# Evaluation

Tools: built-in Codex image generation for the image samples; Grok Imagine for video level 1; Canva AI Video Clip for video levels 2–4. Image model version and seeds were not exposed. Scores are one-reviewer judgments; output variation is not measured statistically. The video rows use different services and are not a controlled prompt-level comparison.

| Medium | Level | Output | Quality | Prompt adherence | Coherence | Style match | Observation |
|---|---|---|---:|---:|---:|---:|---|
| Image | 1 Simple | `generated_images/level1_imagegen.png` | 4 | 3 | 4 | N/A | Main subject and watering action are clear; the model added text/signage that the prompt did not request. |
| Image | 2 Detailed | `generated_images/level2_imagegen.png` | 5 | 5 | 5 | 4 | Brass robot, tomato plants, watering can and greenhouse are explicit and visible; warm light supports the requested setting. |
| Image | 3 Style + camera | `generated_images/level3_imagegen.png` | 5 | 5 | 5 | 5 | Cinematic lighting, shallow depth of field and left/right composition are clear. |
| Image | 4 Structured | `generated_images/level4_imagegen.png` | 4 | 5 | 4 | 3 | Subject and composition follow the fields, but the requested storybook watercolor reads closer to a realistic painterly image. |
| Video | 1 Simple | Grok Imagine, 6s at 480p; result remains in the signed-in Grok library | 3 | 3 | 3 | N/A | One browser sample generated for “A robot watering plants.” A visible frame showed a watering can and robot arm over a garden, but no full robot body; the 6-second player was available. The browser download remained incomplete, so no MP4 is included in the repository. Further generations were gated behind a ₹2,900/month plan; no subscription was started. |
| Video | 2 Motion | Canva AI Video Clip | Not scored | Not scored | Not scored | N/A | Clip generated; preview showed a brass robot watering tomatoes in a warm greenhouse. MP4 download was blocked by Edge. [Canva thread](https://www.canva.com/ai/thread/3e01ded7-788e-46b9-bea1-1cdb337f21f6). |
| Video | 3 Camera + timing | Canva AI Video Clip | Not scored | Not scored | Not scored | N/A | Clip generated without audio; Canva said exact 8-second duration is not controllable. Preview showed a robot watering tomatoes in a greenhouse. MP4 download was blocked by Edge. [Canva thread](https://www.canva.com/ai/thread/e995a89e-72cb-43c7-9b0a-e1f9725cc3f8). |
| Video | 4 Shot list | Canva AI Video Clip | Not scored | Not scored | Not scored | N/A | Clip generated without audio. Canva described three requested beats, but a complete timeline could not be verified from the preview. MP4 download was blocked by Edge. [Canva thread](https://www.canva.com/ai/thread/f5fc6c9f-b130-4ca8-b2ae-6a1e5b4af362). |

## Scoring rubric
- Quality: visual clarity and artefacts (5 = strong).
- Prompt adherence: requested elements visibly present (5 = all major elements).
- Coherence: plausible anatomy and scene (5 = consistent).
- Style match: fit to requested style (5 = close). N/A when no style was specified.

## Conclusion
For this four-image sample, adding subject details and action produced the clearest improvement over the short prompt. The camera and composition terms in level 3 were followed well. The structured style label was less reliable: the output looked more photographic than watercolor. One sample per image prompt cannot separate prompt effects from random variation. Video levels 1–4 were generated, but levels 2–4 used Canva after Grok's paid gate, so the cross-level video comparison is confounded by model differences. The Canva MP4 exports were blocked by Edge and are not stored in this repository; their signed-in result links are recorded in `generated_videos/README.md`.
