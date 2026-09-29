# Step-by-step run guide
1. Pick one image tool (e.g. DALL-E, Stable Diffusion, Midjourney) and one video tool you have access to (e.g. Sora, Veo, Runway, Pika). Note tool, version, date.
2. Read `prompt_anatomy.md`; adapt the four levels in `prompts/image_prompts.md` and `prompts/video_prompts.md` if needed. Keep the subject identical across levels.
3. Image runs: use the same tool and, if possible, the same seed/aspect ratio for all four levels. Generate 1-3 variants per level.
4. Save files as `generated_images/<level>_<tool>.png`, e.g. `L1_dalle.png`, `L4_dalle.png`.
5. Video runs: use the same duration and aspect ratio for all levels. Save as `generated_videos/<level>_<tool>.mp4`.
6. Rate each output 1-5 in `evaluation.md` using the rubric. Rate before re-reading the expected-effect column to avoid bias.
7. Add notes on what was ignored, artefacts and consistency problems.
8. Compare with the expected-effect column; note where reality differed.
9. Write the conclusion; commit prompts, outputs and evaluation together.
10. If a tool does not support a feature (e.g. negative prompts or shot lists), write the exclusion in plain words and note this limit.
