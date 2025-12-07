from dsax.search.BinarySearch import binarysearch
from dsax.helpers import animate, _timeit, generate
import random



@animate
def perf_Bsearch():
	for size, arr in generate():
		target = arr[-1]
		time = _timeit(binarysearch, arr, target)
		yield size, time


perf_Bsearch()
