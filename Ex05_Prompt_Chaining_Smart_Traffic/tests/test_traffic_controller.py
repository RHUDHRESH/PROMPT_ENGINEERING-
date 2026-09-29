import os, sys, unittest
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
from traffic_controller import TrafficController


class TestTraffic(unittest.TestCase):
    def setUp(self):
        self.c = TrafficController()

    def test_green_bounds(self):
        self.assertEqual(self.c.green_time(0), 10)
        self.assertEqual(self.c.green_time(100), 60)
        self.assertEqual(self.c.green_time(15), 30)

    def test_negative_queue(self):
        with self.assertRaises(ValueError):
            self.c.green_time(-1)

    def test_longest_queue_first(self):
        self.assertEqual(self.c.next_phase({"N": 1, "E": 9, "S": 2, "W": 3}), "E")

    def test_emergency_preempts(self):
        self.assertEqual(self.c.next_phase({"N": 50, "E": 0, "S": 0, "W": 0}, emergency="W"), "W")

    def test_starvation_prevented(self):
        q = {"N": 50, "E": 1, "S": 0, "W": 0}
        served = [self.c.next_phase(q) for _ in range(5)]
        self.assertIn("E", served)

    def test_bad_input(self):
        with self.assertRaises(ValueError):
            self.c.next_phase({"N": 1})
        with self.assertRaises(ValueError):
            TrafficController(min_green=0)


if __name__ == "__main__":
    unittest.main()
