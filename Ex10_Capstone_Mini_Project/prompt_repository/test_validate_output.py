import copy
import json
import os
import re
import unittest

from validate_output import validate

HERE = os.path.dirname(os.path.abspath(__file__))

GOOD = {
    "summary": "Irrigate at dawn.",
    "actions": [{"priority": 1, "action": "Irrigate 6 mm", "why": "Dry soil", "cost": "low"}],
    "risks": ["Forecast may change"],
    "confidence": "medium",
    "questions": [],
}


class ValidatorTests(unittest.TestCase):
    def test_good(self):
        self.assertEqual(validate(GOOD), [])
        self.assertEqual(validate(json.dumps(GOOD)), [])

    def test_fenced_json(self):
        self.assertEqual(validate("```json\n%s\n```" % json.dumps(GOOD)), [])

    def test_not_json(self):
        self.assertTrue(validate("Sure! Here is advice"))

    def test_missing_key(self):
        d = copy.deepcopy(GOOD)
        del d["risks"]
        self.assertTrue(validate(d))

    def test_extra_key(self):
        d = copy.deepcopy(GOOD)
        d["notes"] = "x"
        self.assertTrue(validate(d))

    def test_bad_cost(self):
        d = copy.deepcopy(GOOD)
        d["actions"][0]["cost"] = "cheap"
        self.assertTrue(validate(d))

    def test_bad_confidence(self):
        d = copy.deepcopy(GOOD)
        d["confidence"] = "very high"
        self.assertTrue(validate(d))

    def test_bad_priority(self):
        d = copy.deepcopy(GOOD)
        d["actions"][0]["priority"] = "1"
        self.assertTrue(validate(d))

    def test_too_many_questions(self):
        d = copy.deepcopy(GOOD)
        d["questions"] = ["a?", "b?", "c?", "d?"]
        self.assertTrue(validate(d))

    def test_priority_order(self):
        d = copy.deepcopy(GOOD)
        d["actions"].append({"priority": 1, "action": "x", "why": "y", "cost": "low"})
        self.assertTrue(validate(d))

    def test_sample_outputs_all_valid(self):
        blocks = []
        for name in ("sample_outputs.md", "sample_outputs_part2.md"):
            with open(os.path.join(HERE, name), encoding="utf-8") as f:
                blocks += re.findall(r"```json\n(.*?)\n```", f.read(), re.S)
        self.assertEqual(len(blocks), 30)
        for i, b in enumerate(blocks, 1):
            self.assertEqual(validate(b), [], "sample %d invalid" % i)


if __name__ == "__main__":
    unittest.main()
