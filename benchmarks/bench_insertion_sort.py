from algox.sort import insertion_sort
from algox.helpers import generate, benchmark, animate


@animate
def bench_insertion_sort():
    for size, arr in generate():
        time, mem = benchmark(insertion_sort, arr)
        yield size, time, mem


bench_insertion_sort()
