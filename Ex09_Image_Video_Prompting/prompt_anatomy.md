# Prompt anatomy: image and video

## Image prompt formula
```
[Subject + key traits] + [Action/pose] + [Setting/background] + [Style/medium] + [Lighting] + [Camera/composition] + [Colour/mood] + [Quality tags] + [Negative / exclusions]
```
Example: `Small brass robot (subject) watering tomatoes with a copper can (action), Victorian greenhouse in morning fog (setting), watercolour illustration (style), soft god rays (lighting), medium shot, subject on left third (camera), warm greens and brass (colour), highly detailed (quality). Negative: text, watermark, extra limbs.`

## Video prompt formula
```
[Subject] + [Action/motion] + [Setting] + [Camera movement + shot size] + [Lighting/style] + [Duration/pacing] + [Audio if supported] + [Consistency notes] + [Avoid]
```
Example: `A brass robot waters tomato plants (subject+action) in a foggy greenhouse (setting); slow dolly-in, medium shot (camera); cinematic, warm light (style); 8 seconds (duration); soft ambient sound (audio); same robot design throughout (consistency); avoid text and morphing hands.`

## Vocabulary
**Shot size:** extreme wide, wide/establishing, medium, close-up, extreme close-up.
**Angle:** eye level, low angle, high angle, bird's-eye, over-the-shoulder, Dutch tilt.
**Camera movement:** static, pan, tilt, dolly in/out, tracking, truck, crane/jib, handheld, orbit, zoom, rack focus.
**Lens/DOF:** wide-angle, 35 mm, 85 mm portrait, telephoto, macro, shallow or deep depth of field.
**Motion words:** gentle sway, arcing water, slow-motion, time-lapse, drifting, accelerating, loop.
**Lighting:** golden hour, backlight, rim light, soft diffuse, hard noon sun, volumetric/god rays, low key, high key.
**Style:** photorealistic, cinematic, watercolour, anime-inspired, claymation, 3D render, documentary. Naming a living artist or copyrighted character raises ethical/policy issues; prefer generic style descriptions.

## Levels used in this exercise
| Level | Adds | Expected risk |
|---|---|---|
| 1 Simple | subject only | model fills in everything randomly |
| 2 Detailed / Motion | traits, setting, basic motion | style still random |
| 3 Style+camera / Camera+timing | look, lens, camera move, duration | some elements may be ignored |
| 4 Structured / Shot list | labelled fields or per-shot timing | best control; longer prompts can still lose details, video shot-by-shot may drift in character design |

## Video-specific tips
- One main action per shot; complex multi-step actions often fail.
- Describe camera movement separately from subject movement.
- Short clips (a few seconds) are more consistent than long ones.
- Repeat identical character description in every shot for consistency.
- Tool limits (max duration, audio support, shot lists) vary; check the tool's current docs.
