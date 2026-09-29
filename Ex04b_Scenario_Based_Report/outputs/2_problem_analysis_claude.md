# Problem analysis - chain of thought - Claude output
Tool: Claude, answered directly (not ChatGPT). Text below the line is the section as used in report.md.

---

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
