# Video generation record

Four prompt levels were run across two services. Level 1 used Grok Imagine; levels 2–4 used Canva AI Video Clip on 2026-09-29. Canva generated three clips, but its `Save Video` action opened a media URL that Edge blocked (`ERR_BLOCKED_BY_CLIENT`), so no MP4 files could be added here. The Canva AI threads remain in the signed-in Canva account; their URLs are below and may require that account to open.

| Level | Prompt | Service and result | Canva AI thread |
|---|---|---|---|
| 1 Simple | `A robot watering plants` | Grok Imagine; 6 seconds, 480p. A visible frame showed a watering can and robot arm over a garden, without a full robot body. The earlier download was incomplete. | Grok result remained in the signed-in Grok library. |
| 2 Motion | `A small brass robot waters tomato plants, water arcs from the can, leaves sway` | Canva AI generated a silent clip. The preview showed a brass robot watering tomato plants in a warmly lit greenhouse. | [Canva AI result](https://www.canva.com/ai/thread/3e01ded7-788e-46b9-bea1-1cdb337f21f6) |
| 3 Camera + timing | `Slow dolly-in on a brass robot watering tomatoes in a foggy greenhouse; 8 seconds; light rays flicker; gentle ambient audio` | Canva AI generated the clip without audio because audio required Ultra AI. Canva said the exact 8-second duration was not controllable. The preview showed a robot watering tomatoes in a greenhouse. | [Canva AI result](https://www.canva.com/ai/thread/e995a89e-72cb-43c7-9b0a-e1f9725cc3f8) |
| 4 Shot list | Three-shot sequence from `prompts/video_prompts.md` | Canva AI generated a silent clip and described all three requested beats. Its preview frame alone does not verify the complete shot sequence or duration. | [Canva AI result](https://www.canva.com/ai/thread/f5fc6c9f-b130-4ca8-b2ae-6a1e5b4af362) |

## Limitations

All four prompt levels now have a generated clip, but levels 1 and 2–4 used different services, so this is not a controlled comparison of prompt complexity. Canva warned that its monthly AI limit was nearly reached after level 4. No paid plan or account signup was used. The MP4 files are not present because Edge blocked Canva's download URL; inspect the saved Canva AI thread previews while signed in. No audio was produced for levels 2–4.
