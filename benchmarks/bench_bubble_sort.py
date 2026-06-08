from algox.sort import bubble_sort
from algox.helpers import animate, benchmark, generate


@animate
def bench_bubble_sort():
    for size, arr in generate(upper=2000, step=20):
        time, mem = benchmark(bubble_sort, arr)
        yield size, time, mem


bench_bubble_sort()
