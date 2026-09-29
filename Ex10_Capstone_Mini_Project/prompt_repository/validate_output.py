#!/usr/bin/env python3
"""Validate an AgriAdvisor JSON reply against the schema in system.md.

Schema:
{"summary": str,
 "actions": [{"priority": int>=1, "action": str, "why": str, "cost": "low|med|high"}],
 "risks": [str], "confidence": "high|medium|low", "questions": [str] (max 3)}

Usage: python3 validate_output.py reply.json   (or pipe JSON on stdin)
Checks structure only, not agronomic correctness.
"""
import json
import re
import sys

TOP_KEYS = {"summary", "actions", "risks", "confidence", "questions"}
ACTION_KEYS = {"priority", "action", "why", "cost"}
COSTS = {"low", "med", "high"}
CONFIDENCE = {"high", "medium", "low"}
MAX_QUESTIONS = 3


def _strip_fence(text):
    m = re.match(r"^\s*```(?:json)?\s*(.*?)\s*```\s*$", text, re.S)
    return m.group(1) if m else text


def validate(reply):
    """Return a list of error strings (empty list means valid).

    `reply` may be a JSON string or an already parsed dict.
    """
    if isinstance(reply, str):
        try:
            data = json.loads(_strip_fence(reply))
        except json.JSONDecodeError as exc:
            return ["invalid JSON: %s" % exc]
    else:
        data = reply
    if not isinstance(data, dict):
        return ["top level must be an object"]

    errors = []
    missing = TOP_KEYS - data.keys()
    extra = data.keys() - TOP_KEYS
    if missing:
        errors.append("missing keys: %s" % sorted(missing))
    if extra:
        errors.append("unexpected keys: %s" % sorted(extra))

    def is_str(v):
        return isinstance(v, str) and v.strip() != ""

    if "summary" in data and not is_str(data["summary"]):
        errors.append("summary must be a non-empty string")

    actions = data.get("actions")
    if "actions" in data:
        if not isinstance(actions, list):
            errors.append("actions must be a list")
        else:
            priorities = []
            for i, a in enumerate(actions):
                p = "actions[%d]" % i
                if not isinstance(a, dict):
                    errors.append("%s must be an object" % p)
                    continue
                if a.keys() != ACTION_KEYS:
                    errors.append("%s keys must be exactly %s" % (p, sorted(ACTION_KEYS)))
                pr = a.get("priority")
                if isinstance(pr, bool) or not isinstance(pr, int) or pr < 1:
                    errors.append("%s.priority must be an integer >= 1" % p)
                else:
                    priorities.append(pr)
                for k in ("action", "why"):
                    if k in a and not is_str(a[k]):
                        errors.append("%s.%s must be a non-empty string" % (p, k))
                if a.get("cost") not in COSTS:
                    errors.append("%s.cost must be one of %s" % (p, sorted(COSTS)))
            if priorities != sorted(priorities):
                errors.append("actions must be ordered by priority")
            if len(set(priorities)) != len(priorities):
                errors.append("priorities must be unique")

    for key in ("risks", "questions"):
        if key in data:
            v = data[key]
            if not isinstance(v, list) or not all(is_str(x) for x in v):
                errors.append("%s must be a list of non-empty strings" % key)

    if "confidence" in data and data["confidence"] not in CONFIDENCE:
        errors.append("confidence must be one of %s" % sorted(CONFIDENCE))

    q = data.get("questions")
    if isinstance(q, list) and len(q) > MAX_QUESTIONS:
        errors.append("at most %d questions allowed" % MAX_QUESTIONS)

    return errors


def main(argv):
    text = open(argv[1], encoding="utf-8").read() if len(argv) > 1 else sys.stdin.read()
    errors = validate(text)
    if errors:
        print("INVALID")
        for e in errors:
            print(" -", e)
        return 1
    print("VALID")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
