from dsax.sort.SelectionSort import selection_sort
from dsax.helpers import animate, _timeit, generate
import random

@animate
def perf_SelectionSort():
	for size, arr in generate(step=10):
		time = _timeit(selection_sort, arr)
		yield size, time

perf_SelectionSort()
