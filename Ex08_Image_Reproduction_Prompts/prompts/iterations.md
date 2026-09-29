# Prompt iterations
Tool used: ________  Seed/settings: ________ (fill when you generate)

> The v1-v4 below are a **worked example on a sample landscape (replace with your assigned image)**. No images have been generated for them. Keep the same seed/settings between versions where the tool allows, so changes come from the prompt only.

## v1 - Basic
```
A sunset over a mountain range
```
Intent: baseline; see what the model assumes by default.

## v2 - Details (colours, shapes, textures, style)
```
A sunset over purple mountains, golden sky, a calm river winding through the valley, soft mist, photorealistic
```
Added: colours, secondary object (river), atmosphere, style.

## v3 - Composition + lighting + camera
```
Wide-angle landscape photo, low sun on the horizon backlighting layered purple mountain ridges, warm golden-hour light, reflective river in the foreground leading the eye to the peaks, shallow haze, 16:9, high detail
```
Added: lens/framing, light direction, leading line, aspect ratio.

## v4 - Correction from observed differences
Corrections below are **hypothetical** (what one might fix after seeing typical outputs); rewrite after you really compare v3 with your reference.
```
Wide-angle landscape photo at eye level, horizon on the upper third, low sun hidden just behind layered purple mountain ridges with pale pink upper sky, warm golden-hour rim light on ridge edges, calm reflective river entering bottom-left and winding to the peaks, a few pine trees on the left bank, thin low mist between ridges, deep depth of field, 16:9, high detail
```
Negative prompt (if supported): `blurry, oversaturated, text, watermark, people, buildings, lens flare`

## Change log
| From -> To | What was added | Why |
|---|---|---|
| v1 -> v2 | colours, river, mist, style | v1 leaves everything to the model |
| v2 -> v3 | camera, light direction, composition | control framing and mood |
| v3 -> v4 | horizon position, sky colour, trees, river direction, negatives | pin down details that usually drift |
