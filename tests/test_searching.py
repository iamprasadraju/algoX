import unittest
from algox.search import binary_search, linear_search
from algox.helpers import generate


class TestSearching(unittest.TestCase):
    def test_BinarySearch(self):
        for _, arr in generate(sort=True):
            target = arr[-1]
            self.assertEqual(binary_search(arr, target), len(arr) - 1)

    def test_LinearSearch(self):
        for _, arr in generate(sort=True):
            target = arr[-1]
            self.assertEqual(linear_search(arr, target), len(arr) - 1)


if __name__ == "__main__":
    unittest.main()
