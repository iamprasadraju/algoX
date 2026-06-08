import unittest
from algox.sort import selection_sort, bubble_sort, insertion_sort
from algox.helpers import generate


class TestSorting(unittest.TestCase):
    def test_SelectionSort(self):
        for _, arr in generate():
            self.assertEqual(selection_sort(arr), sorted(arr))

    def test_BubbleSort(self):
        for _, arr in generate():
            self.assertEqual(bubble_sort(arr), sorted(arr))

    def test_InsertionSort(self):
        for _, arr in generate():
            self.assertEqual(insertion_sort(arr), sorted(arr))


if __name__ == "__main__":
    unittest.main()
