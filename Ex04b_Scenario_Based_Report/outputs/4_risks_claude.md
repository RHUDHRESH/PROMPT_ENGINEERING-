# Risks and mitigations - few-shot prompt - Claude output
Tool: Claude, answered directly (not ChatGPT). Text below the line is the section as used in report.md.

---

The two examples from the prompt are kept, followed by five new risks.

- Risk: Sensor drift -> Impact: false alarms -> Mitigation: monthly calibration.
- Risk: Poor data quality -> Impact: model misses leaks -> Mitigation: data audit before pilot.
- Risk: Customer data privacy breach (meter-level consumption reveals household behaviour) -> Impact: legal exposure and loss of public trust -> Mitigation: use zone-level pressure/flow data, anonymise or aggregate meter data, apply access controls and a privacy assessment before go-live.
- Risk: Too many false positives -> Impact: crews waste time on dry holes and lose confidence in the tool -> Mitigation: agree a target precision with crews, tune alert thresholds in month 2-3, and report false-alarm rate weekly.
- Risk: Pilot zones not representative of the whole network -> Impact: results overstate or understate real benefit, leading to a wrong rollout decision -> Mitigation: choose zones with mixed pipe age and materials and record their characteristics with the results.
- Risk: Repair crews cannot keep up with detected leaks -> Impact: savings are not realised and detected leaks keep running -> Mitigation: reserve crew capacity for the pilot zones and prioritise repairs by estimated loss.
- Risk: Vendor lock-in or cost overrun -> Impact: budget exceeded or data trapped in one platform -> Mitigation: fixed-price pilot contract, agreed data-export terms and a stage gate at month three.
