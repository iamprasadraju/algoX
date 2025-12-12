import unittest
from dsax.sort import selectionsort
from dsax.helpers import generate

class TestSorting(unittest.TestCase):
	def test_SelectionSort(self):
		for _, arr in generate():
			self.assertEqual(selectionsort(arr, reverse=True), sorted(arr, reverse=True))
	

if __name__ == "__main__":
	unittest.main()