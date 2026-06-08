from algox.search import binary_search
from algox.helpers import animate, benchmark, generate


@animate
def bench_binary_search():
    for size, arr in generate(step=10, sort=True):
        target = arr[-1]
        time, mem = benchmark(binary_search, arr, target)
        yield size, time, mem


bench_binary_search()
