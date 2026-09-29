# Tool comparison notes: DALL-E vs Stable Diffusion vs Midjourney
Only widely documented general facts; features change between versions, so check current docs.

| Aspect | DALL-E (OpenAI) | Stable Diffusion (Stability AI, open weights) | Midjourney |
|---|---|---|---|
| Prompt style | Natural-language sentences; accessible via ChatGPT or API | Keyword/phrase prompts common; long sentences work less consistently on older versions | Short descriptive phrases plus parameters |
| Negative prompt | No dedicated negative field; describe what you want, or state exclusions in the sentence | Yes, a separate negative prompt field in most UIs (e.g. AUTOMATIC1111, ComfyUI) | `--no <thing>` parameter |
| Seed | Not user-controllable in the ChatGPT interface | Yes, user-set seed for reproducibility (with same model/sampler/settings) | `--seed <n>` |
| Aspect ratio | Chosen via size options or stated in the request | Set width/height in the UI | `--ar 16:9` |
| Other controls | Conversational edits/refinement | Sampler, steps, CFG scale, LoRAs, ControlNet, img2img, run locally | `--stylize`, `--chaos`, version flag, image prompts, upscalers |
| Access | Hosted service | Local or hosted; most flexible and technical | Hosted (web/Discord), subscription |

## Practical implications for this exercise
- Stable Diffusion gives the most reproducible comparison across v1-v4 (fixed seed, fixed settings).
- With DALL-E or Midjourney, record the full prompt and parameters and generate several variants per version.
- Record the tool, model version and date in `prompts/iterations.md`.
