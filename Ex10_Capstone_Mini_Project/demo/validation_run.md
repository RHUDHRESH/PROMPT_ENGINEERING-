# Validator run record

Date: 2026-09-29  
Command: `python -m unittest -v` from `prompt_repository/`  
Python: bundled Python runtime available in the Codex workspace

## Result
All 11 validator tests passed, including the test that extracts and validates all 30 JSON sample outputs. The tests also cover malformed JSON, missing/extra keys, invalid priority and confidence fields, too many questions and ordering.

This run verifies schema and formatting behaviour only. It does not verify the farming advice, safety or local suitability. It is a command-line validation demonstration, not a live-model screen recording.
