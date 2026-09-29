# Exp-7: Prompt-Based Personal Productivity Assistant

**Due:** 25 Sep 2026 · **Reference repo:** RaajaThilahar/Ex.No.7

## Features
- **Task manager** — natural-language input ("Remind me to call mom at 6 PM"), priorities, daily summary
- **Smart scheduler** — events, overlap detection, free-slot finder
- **Wellness tips** — adapts to 👍/👎 feedback (stored preferences = memory)
- **LLM mode (optional)** — paste `prompts/system_prompt.md` into any LLM chat to use the same assistant conversationally; the CLI itself is fully offline.

## Run
```
cd src && python3 assistant.py          # interactive CLI
python3 -m unittest discover -s tests   # tests (from this folder)
```
Commands: `add <text>`, `list`, `summary`, `schedule <title> <HH:MM> <minutes>`, `free`, `tip`, `like`, `dislike`, `quit`.

## Files
| File | Purpose |
|---|---|
| `prompts/system_prompt.md` | System prompt + per-task prompts for an LLM |
| `src/assistant.py` | CLI + core logic |
| `src/memory.json` | Auto-created preference store (git-ignored) |
| `tests/` | Unit tests |
| `requirements.md` | Core requirements |
| `feedback.md` | User feedback log + adaptations |
