import time
from generic_search import linear_contains, binary_contains


def time_linear_contains():
    one_million = range(1, 1000000)

    tic = time.perf_counter()
    linear_contains(one_million, 503883)
    toc = time.perf_counter()
    timed = f"{toc-tic:.06f}"
    print(f'That took {timed} seconds')


def time_binary_contains():
    one_million = range(1, 1000000)
    tic = time.perf_counter()
    binary_contains(one_million, 503883)
    toc = time.perf_counter()
    timed = f"{toc-tic:.06f}"
    print(f'That took {timed} seconds')
