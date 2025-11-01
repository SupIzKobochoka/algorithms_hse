import numpy as np
import sys
sys.setrecursionlimit(100_000_000)

def tests(quicksearch):
    rng = np.random.default_rng(42)
    for _ in range(100):
        k = rng.integers(1, 101)
        arr = rng.random(1000).tolist()
        answer = sorted(arr, reverse=True)[k-1]
        pred = quicksearch(arr, k=k)

        assert answer==pred, f'with \nrng = np.random.default_rng(42) (attempt={_}) arr = rng.random(1000)\n got wrong answer'

    assert 1 == quicksearch([1], k=1), f'with [1] expected 1 got {quicksearch([1], k=1)}'