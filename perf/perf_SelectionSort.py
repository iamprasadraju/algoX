from dsax.sort import selectionsort
from dsax.helpers import animate, _timeit, generate
import random

@animate
def perf_SelectionSort(step=50):
	for size, arr in generate(upper_limit= 2000):
		time = _timeit(selectionsort, arr)
		yield size, time

perf_SelectionSort()
