import numpy as np
import sys
sys.setrecursionlimit(100_000_000)

def tests(quicksort, mergesort):
    rng = np.random.default_rng(69)
    for _ in range(100):
        arr = rng.random(1000).tolist()
        arr1 = arr.copy()
        arr2 = arr.copy()
        answer = sorted(arr1)

        assert answer==quicksort(arr1)[0]==mergesort(arr2)[0], f'with \nrng = np.random.default_rng({_}) arr = rng.random(1000)\n got wrong answer'

    # На уже отосртированном списке quick sort работать будет сильно дольше, потому что будет постоянно делить части [n-1, 1]
    rng = np.random.default_rng(142)
    arr = sorted(rng.random(2000).tolist())
    arr1 = arr.copy()
    arr2 = arr.copy()
    _, quicksort_time = quicksort(arr1)
    _, mergesort_time = mergesort(arr2)

    print(f'with sorted array length=3000:{quicksort_time=:.5f}, {mergesort_time=:.5f}')