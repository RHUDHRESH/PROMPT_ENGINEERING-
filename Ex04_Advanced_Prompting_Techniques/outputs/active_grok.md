# Active Prompting: Grok Browser Runs

Date: 2026-09-29. Tool: Grok Fast in the user's existing Edge session. Each baseline prompt was submitted once and regenerated to collect five answer variants. The exemplar prompt was then submitted as a new conversation and regenerated until five variants were collected. Decisions below are transcribed from the visible browser results; incomplete response endings are marked. Exact model seed and token counts were not exposed.

## Drone navigation

**Baseline prompt:** Should a drone with 20 min battery, carrying a 1 kg payload, 6 km from base and facing 8 m/s headwind, continue the mission or return? Answer CONTINUE or RETURN and give a one-line reason.

**Five baseline decisions:** RETURN, RETURN, RETURN, RETURN, RETURN (5/5). The rationales varied: headwind and payload reduce the energy margin; a return may consume the remaining endurance; one answer assumed the return leg would have a tailwind. One response ended mid-sentence. These assumptions cannot be resolved from the prompt because airspeed, power draw, wind direction along the full route, and safety reserve are missing.

**Human-written exemplar:**

> Q: Should a drone with 20 min battery, carrying a 1 kg payload, 6 km from base and facing 8 m/s headwind, continue the mission or return?  
> Reasoning: The prompt omits airspeed, battery consumption under load, wind variability and required reserve, so a safe round-trip margin cannot be verified. Use the conservative failsafe when the remaining-energy margin is unknown.  
> A: RETURN.

**Five exemplar-guided decisions:** RETURN, RETURN, RETURN, RETURN, RETURN (5/5). Reasons consistently noted that the missing energy inputs prevent verifying a safe return margin.

## Smart irrigation

**Baseline prompt:** Skip watering if 3 mm rain is forecast but soil is at 12%? Answer WATER or SKIP and give a one-line reason.

**Five baseline decisions:** WATER, WATER, WATER, WATER, WATER (5/5). Rationales said the forecast rain may be too light or uncertain to relieve low soil moisture; two responses visibly ended mid-sentence.

**Human-written exemplar:**

> Q: Skip watering if 3 mm rain is forecast but soil is at 12%?  
> Reasoning: Check the crop-specific moisture trigger, soil, rain timing and sensor reliability. If 12% is below the validated trigger, a short calibrated dose followed by a recheck is safer than skipping solely because 3 mm is forecast.  
> A: WATER.

**Five exemplar-guided decisions:** WATER, WATER, WATER, WATER, WATER (5/5). The responses repeated the need for a short dose/recheck and noted that the forecast may not reach the root zone.

## Robot path planning

**Baseline prompt:** Replan or continue when a new obstacle appears 1 cell ahead? Answer REPLAN or CONTINUE and give a one-line reason.

**Five baseline decisions:** REPLAN, REPLAN, REPLAN, REPLAN, REPLAN (5/5). Reasons consistently said the immediate path is blocked, so continuing risks collision and the map/path should be updated.

**Human-written exemplar:**

> Q: Replan or continue when a new obstacle appears 1 cell ahead?  
> Reasoning: The next move would enter a newly occupied cell. Stop before it, update the map and compute a collision-free path that respects robot clearance.  
> A: REPLAN.

**Five exemplar-guided decisions:** REPLAN, REPLAN, REPLAN, REPLAN, REPLAN (5/5). Exemplar-guided reasons retained the stop, map update and safe-path steps.

## Observation and limits

All three decisions were already unanimous at baseline, so the exemplar did not improve binary decision consistency (5/5 before and after). It made rationales more cautious and specific for the drone and irrigation cases. These are single-model, single-session observations; repeated generations may share hidden system context, and regeneration variants are not independent laboratory trials. Grok searched the web for some answers, response latency and token counts were not recorded, and some rationales were cut off in the interface. Check engineering decisions against domain data before use.