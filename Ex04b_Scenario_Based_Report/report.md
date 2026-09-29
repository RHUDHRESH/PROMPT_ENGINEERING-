# AI Leak Detection Pilot — Board Report

*Prepared for the Board of Directors. Decision requested: approve a 6-month pilot. Draft written by Claude from the scenario in `scenario.md`; sections were produced with different prompting techniques (see `prompts/` and `outputs/`).*

> **Facts vs assumptions.** The only facts taken from the scenario are: rising pipe leaks, about 30% non-revenue water, a 6-month pilot, a limited budget and a data-privacy constraint. Everything else marked "illustrative" (the split of the 30% by cause, option ratings, roles and timings) is an assumption for discussion and must be replaced with the water board's own data and supplier quotes before a funding decision.

## 1. Executive summary

Roughly 30% of the water we treat is lost before it earns revenue, and rising pipe leaks are a growing part of that. Today we find leaks mainly by manual surveys and customer reports, so many run for weeks unseen. We propose a six-month, limited-budget pilot of AI-based leak detection in one or two selected zones. Machine-learning models will analyse pressure and flow data to flag likely leaks, and crews will verify and repair them. The pilot will show whether the approach finds leaks faster, cuts water losses and pays back, without exposing customer data. We ask the Board to approve the pilot and to judge it against clear targets at month six before deciding on wider rollout.

## 2. Problem analysis

**Step 1 - what non-revenue water (NRW) is.** NRW is water put into the network that is never billed. It is made up of (a) real losses (physical leakage and overflows), (b) apparent losses (water used but not measured or billed) and (c) unbilled authorised use (flushing, firefighting).

**Step 2 - causes and estimated share of the 30%.** The scenario gives only the 30% total. The split below is an **illustrative assumption** based on typical utility water balances, not this Board's data; it should be replaced by the water board's own water audit.

| Rank | Cause | Category | Assumed share of NRW | Approx. points of the 30% |
|---|---|---|---|---|
| 1 | Leaks on mains and service connections (ageing pipes, pressure surges) | Real loss | 60% | 18 |
| 2 | Customer-meter under-registration | Apparent loss | 17% | 5 |
| 3 | Illegal connections and theft | Apparent loss | 10% | 3 |
| 4 | Billing and data-handling errors | Apparent loss | 7% | 2 |
| 5 | Unbilled authorised use (flushing, firefighting) | Unbilled authorised | 6% | 2 |

**Step 3 - what AI can address.**
- **Leakage (rank 1): strongly.** Models on pressure and flow data can spot the signature of new leaks early and narrow the search area, so crews go to the right place sooner. Faster detection also cuts the running time of each leak.
- **Meter under-registration and theft (ranks 2-3): partly.** Consumption-pattern anomaly detection can flag suspect connections, but this is outside the pilot's core scope.
- **Billing errors and unbilled authorised use (ranks 4-5): little.** These are process problems, better fixed by data clean-up and policy.

**Conclusion:** if the illustrative split is roughly right, leakage is the largest and most AI-addressable cause, so a pilot focused on leak detection targets the biggest share of the problem. Even a modest improvement there would be material.

## 3. Options compared

The ratings are **qualitative and illustrative**, based on general industry experience, because no local quotes or trial data were provided. Costs are relative, not dollar figures; real values need supplier quotes.

| Option | Cost | Accuracy | Time to deploy | Data needed | Risk |
|---|---|---|---|---|---|
| Manual survey (crews with listening equipment) | Low equipment cost, high ongoing labour | Medium; depends on crew skill, mostly finds existing leaks | Immediate (weeks) | None beyond network maps | Slow and periodic; limited coverage; leaks run between surveys |
| Acoustic sensors (loggers on valves and hydrants) | Medium to high (hardware, installation, maintenance) | High for locating leaks on metal pipes; weaker on plastic pipes | 2-4 months for a zone | Acoustic signals; pipe material and map | Sensor drift, battery life, vandalism; poor performance on plastic pipe |
| Satellite imagery | Medium per survey; no field hardware | Low to medium; indicates suspect areas, not exact points | Weeks to a few months | Imagery plus network map | Coarse resolution, false positives, weather; best as a screening tool |
| ML on pressure/flow data | Low to medium if existing zone meters and SCADA are used; higher if new meters are needed | Medium to high for detecting a leak in a zone; needs field work to pinpoint | 2-4 months (data audit, training, validation) | Historic and live pressure and flow, GIS, repair records | Data quality, false alarms, model drift, privacy if meter-level data is used |

**Reading the table:** no option is best on every criterion. ML on pressure data is cheapest per area covered and best for early detection, while acoustic loggers are the best way to pinpoint the leak once a zone is flagged. Manual crews remain essential for verification.

## 4. Risks and mitigations

The two examples from the prompt are kept, followed by five new risks.

- Risk: Sensor drift -> Impact: false alarms -> Mitigation: monthly calibration.
- Risk: Poor data quality -> Impact: model misses leaks -> Mitigation: data audit before pilot.
- Risk: Customer data privacy breach (meter-level consumption reveals household behaviour) -> Impact: legal exposure and loss of public trust -> Mitigation: use zone-level pressure/flow data, anonymise or aggregate meter data, apply access controls and a privacy assessment before go-live.
- Risk: Too many false positives -> Impact: crews waste time on dry holes and lose confidence in the tool -> Mitigation: agree a target precision with crews, tune alert thresholds in month 2-3, and report false-alarm rate weekly.
- Risk: Pilot zones not representative of the whole network -> Impact: results overstate or understate real benefit, leading to a wrong rollout decision -> Mitigation: choose zones with mixed pipe age and materials and record their characteristics with the results.
- Risk: Repair crews cannot keep up with detected leaks -> Impact: savings are not realised and detected leaks keep running -> Mitigation: reserve crew capacity for the pilot zones and prioritise repairs by estimated loss.
- Risk: Vendor lock-in or cost overrun -> Impact: budget exceeded or data trapped in one platform -> Mitigation: fixed-price pilot contract, agreed data-export terms and a stage gate at month three.

## 5. Recommendation

We recommend that the Board approve a six-month pilot of ML leak detection on pressure and flow data in one or two zones, using acoustic loggers and crews to pinpoint and verify leaks.

- **Run a data audit and select pilot zones.** Owner: Head of Network Operations. Deadline: end of month 1.
- **Build and validate the model, with privacy sign-off.** Owner: Data and IT lead with the Data Protection Officer. Deadline: end of month 3 (stage gate).
- **Verify alerts in the field, repair leaks and report results.** Owner: Pilot project manager. Deadline: month 6 Board meeting.

Expected savings: if the pilot finds and repairs leaks earlier, it should reduce the leakage share of the 30% non-revenue water in the pilot zones, with the size of the saving to be measured against the baseline established in month 1.

## Appendix: assumptions and open items

- The cause split of non-revenue water (60/17/10/7/6%) is illustrative, not measured.
- Option costs, accuracy and deployment times are qualitative industry-style ratings; no quotes, dollar values or trial results were available.
- Pilot budget, zone selection, owners' job titles and the month deadlines are proposals, not existing commitments.
- Expected savings are deliberately not quantified; the month-1 baseline will set the measurable target.
