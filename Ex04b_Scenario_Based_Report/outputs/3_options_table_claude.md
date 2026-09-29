# Options comparison - tabular prompt - Claude output
Tool: Claude, answered directly (not ChatGPT). Text below the line is the section as used in report.md.

---

The ratings are **qualitative and illustrative**, based on general industry experience, because no local quotes or trial data were provided. Costs are relative, not dollar figures; real values need supplier quotes.

| Option | Cost | Accuracy | Time to deploy | Data needed | Risk |
|---|---|---|---|---|---|
| Manual survey (crews with listening equipment) | Low equipment cost, high ongoing labour | Medium; depends on crew skill, mostly finds existing leaks | Immediate (weeks) | None beyond network maps | Slow and periodic; limited coverage; leaks run between surveys |
| Acoustic sensors (loggers on valves and hydrants) | Medium to high (hardware, installation, maintenance) | High for locating leaks on metal pipes; weaker on plastic pipes | 2-4 months for a zone | Acoustic signals; pipe material and map | Sensor drift, battery life, vandalism; poor performance on plastic pipe |
| Satellite imagery | Medium per survey; no field hardware | Low to medium; indicates suspect areas, not exact points | Weeks to a few months | Imagery plus network map | Coarse resolution, false positives, weather; best as a screening tool |
| ML on pressure/flow data | Low to medium if existing zone meters and SCADA are used; higher if new meters are needed | Medium to high for detecting a leak in a zone; needs field work to pinpoint | 2-4 months (data audit, training, validation) | Historic and live pressure and flow, GIS, repair records | Data quality, false alarms, model drift, privacy if meter-level data is used |

**Reading the table:** no option is best on every criterion. ML on pressure data is cheapest per area covered and best for early detection, while acoustic loggers are the best way to pinpoint the leak once a zone is flagged. Manual crews remain essential for verification.
