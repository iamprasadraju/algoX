from algox.sort import selection_sort
from algox.helpers import benchmark, generate, animate


@animate
def bench_selection_sort():
    for size, arr in generate():
        time, mem = benchmark(selection_sort, arr)
        yield size, time, mem


bench_selection_sort()
