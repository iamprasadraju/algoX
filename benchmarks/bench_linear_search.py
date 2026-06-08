from algox.search import linear_search
from algox.helpers import animate, generate, benchmark


@animate
def bench_linear_search():
    for size, arr in generate():
        target = arr[-1]
        time, mem = benchmark(linear_search, arr, target)
        yield size, time, mem


bench_linear_search()
