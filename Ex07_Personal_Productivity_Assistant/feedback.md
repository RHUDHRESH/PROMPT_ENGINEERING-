# User feedback log

**All four sessions below are SIMULATED.** No real users tested the assistant. Each session is a real run of the actual CLI (`src/assistant.py`, `tip` / `like` / `dislike` commands) driven by a scripted "persona" that gives feedback by a fixed rule. Tip categories are chosen randomly by the CLI, so the sequences are one sample, not an average, and re-running gives different sequences. The memory file was deleted between personas (Session 2 continues Session 1's memory on purpose). Run date 2026-09-29. The sequences of tips and feedback come from the runs; the "Observed" and "Adaptation" text is my reading of them.

A real transcript of a normal session (tasks, scheduling, one tip cycle) is in `sample_session.txt`.

| # | Simulated user (rule) | What happened (observed) | Adaptation made / limitation seen |
|---|---|---|---|
| 1 | "Asha", day 1, fresh memory. Likes exercise tips, dislikes screen tips, ignores others. 8 tips | Sequence: hydration, hydration (no feedback), screen (disliked), then exercise x5 (each liked). Final memory: liked {exercise: 5}, disliked {screen: 1} | Weights become `1 + 2*likes`: exercise weight 11 vs 1 for each other category. Only one dislike so screen is still eligible, since the code needs 2 dislikes to exclude a category. Nothing was changed in the code in response |
| 2 | "Asha", day 2, memory kept from Session 1. Likes exercise, no dislikes. 12 tips | Exercise was shown 11 of 12 times, hydration once, screen never (by chance; it was still eligible with weight 1). Memory: liked {exercise: 16} | Adaptation works but is very strong: likes never decay, so variety collapses. Suggested improvement (not implemented): cap the like weight or decay it, or add a small exploration floor |
| 3 | "Ben", fresh memory. Likes hydration, dislikes exercise and screen. 12 tips | Sequence: screen (dis), screen (dis), exercise (dis), exercise (dis), then hydration x8 (liked). Final memory: liked {hydration: 8}, disliked {screen: 2, exercise: 2} | Clear adaptation: after 2 dislikes each, screen and exercise were excluded and only hydration appeared. This matches the requirement "never repeat a disliked tip category" only after 2 dislikes, not 1 |
| 4 | "Cara", fresh memory. Dislikes every category. 12 tips | Tips kept coming from all three categories (hydration 5, screen 4, exercise 3), all disliked. Final memory: disliked {hydration: 5, screen: 4, exercise: 3} | Edge case: once every category has 2 or more dislikes, the code falls back to equal weights and shows everything again. Nothing better can be offered with only 3 categories; a real fix would be to add tip categories or offer to stop tips (not implemented) |

## Summary of what the simulation showed
- The like/dislike memory does change what is shown, and persists across runs through `memory.json` (Sessions 1 to 2).
- Threshold behaviour: 2 dislikes exclude a category; 1 dislike changes nothing.
- Weaknesses found: like weights grow without bound (Session 2), and the all-disliked fallback (Session 4).
- The system prompt in `prompts/system_prompt.md` says "never repeat a disliked tip category", which is stricter than the CLI's behaviour above.
- These findings come from simulated personas and single random runs. They are not evidence of how real users would react.
