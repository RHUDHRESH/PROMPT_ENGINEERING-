import os, sys, tempfile, unittest
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
from assistant import Assistant, parse_task


class T(unittest.TestCase):
    def setUp(self):
        self.a = Assistant(os.path.join(tempfile.mkdtemp(), "m.json"))

    def test_parse(self):
        t = parse_task("Remind me to call mom at 6 PM")
        self.assertEqual((t["title"], t["time"], t["priority"]), ("call mom", "18:00", "medium"))
        self.assertEqual(parse_task("urgent: submit report by 09:30")["priority"], "high")

    def test_order(self):
        self.a.add_task("someday read a book")
        self.a.add_task("urgent pay bill")
        self.assertEqual(self.a.list_tasks()[0]["title"], "urgent pay bill")

    def test_overlap_and_free(self):
        self.a.schedule("Standup", "10:00", 30)
        self.assertIn("overlaps", self.a.schedule("Call", "10:15", 30))
        self.assertEqual(self.a.free_slots()[0], "09:00-10:00")

    def test_feedback_adapts(self):
        self.a.tip()
        cat = self.a.data["last_tip"]
        self.a.feedback(True)
        self.assertEqual(self.a.data["liked"][cat], 1)


if __name__ == "__main__":
    unittest.main()
