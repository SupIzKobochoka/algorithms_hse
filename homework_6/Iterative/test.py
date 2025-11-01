import numpy as np
# import sys
# sys.setrecursionlimit(100_000_000)

def tests(quicksort, mergesort):
    rng = np.random.default_rng(42)
    for _ in range(100):
        arr = rng.random(1000).tolist()
        arr1 = arr.copy()
        arr2 = arr.copy()
        answer = sorted(arr1)

        assert answer==quicksort(arr1)[0]==mergesort(arr2)[0], f'with \nrng = np.random.default_rng({_}) arr = rng.random(1000)\n got wrong answer'

    arr = [1]
    arr1 = arr.copy()
    arr2 = arr.copy()

    assert arr==quicksort(arr1)[0]==mergesort(arr2)[0], f'with [1] expected [1], got {arr1} and {arr2}'