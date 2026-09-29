import os, sys, unittest
sys.path.insert(0, os.path.dirname(__file__))
from binary_search_fixed import binary_search


class T(unittest.TestCase):
    def test_empty(self): self.assertEqual(binary_search([], 1), -1)
    def test_single(self):
        self.assertEqual(binary_search([5], 5), 0)
        self.assertEqual(binary_search([5], 4), -1)
    def test_ends(self):
        a = [1, 3, 5, 7, 9]
        self.assertEqual(binary_search(a, 1), 0)
        self.assertEqual(binary_search(a, 9), 4)
    def test_missing(self):
        a = [1, 3, 5]
        self.assertEqual(binary_search(a, 0), -1)
        self.assertEqual(binary_search(a, 6), -1)
    def test_large(self):
        a = list(range(0, 1_000_000, 2))
        self.assertEqual(binary_search(a, 999_998), 499_999)
        self.assertEqual(binary_search(a, 999_999), -1)


if __name__ == "__main__":
    unittest.main()
