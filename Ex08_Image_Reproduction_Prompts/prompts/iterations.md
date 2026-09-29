# Prompt iterations

Tool used: built-in image generation in Codex. The tool did not expose a repeatable seed. v1 was generated with the sample reference; v2 used v1 as an image reference.

> The reference is `reference_image/sample_reference.png`. The reference itself was generated for this exercise because the course image was not included. These are single samples, not a controlled benchmark.

## Reference creation prompt
```
Use case: reference image for a prompt-engineering lab. Asset type: photorealistic landscape photograph. Primary request: a sunset over a mountain range with a calm river winding from the bottom-left foreground toward the center peaks, and two small pine trees on the left riverbank. Composition: wide 16:9 landscape, eye-level, river as a clear leading line, layered mountain ridges, horizon on upper third. Palette: deep purple mountains, golden-orange horizon, pale pink upper sky, cool teal river shadows. Lighting: low sun hidden behind the ridge, warm rim light, thin mist between ridges. Constraints: no people, buildings, text, logos, borders, or watermark; realistic natural landscape.
```

## v1 - Faithful recreation
```
Create a faithful new image inspired by the reference for an image-prompting experiment. Preserve its wide landscape composition: orange and pink sunset above layered purple mountains, central low sun behind the ridge, mist in the valley, dark pine forest, and a reflective river across the foreground. Keep the river entering from bottom-left and leading toward the center. Photorealistic, 16:9, no text or watermark.
```
Result: `generated_images/v1.png`.

## v2 - Targeted refinement
```
Refine this landscape for closer composition matching. Keep the same mountain silhouettes, river route, pine trees, mist, and warm sunset. Make the horizon sit in the upper third, reduce the brightest orange glow slightly, add a pale pink band to the upper sky, and keep the reflective river entering clearly from the bottom-left. Photorealistic wide 16:9 landscape. Do not add objects, text, or watermark.
```
Result: `generated_images/v2.png`; v1 was supplied as the image reference.

## Change log
| From -> To | What changed | Why |
|---|---|---|
| reference -> v1 | Main colors, objects, river direction, mist, wide framing | Recreate the key visible scene |
| v1 -> v2 | Horizon placement, lighter upper sky, controlled orange brightness | Refine composition and palette while retaining the scene |
