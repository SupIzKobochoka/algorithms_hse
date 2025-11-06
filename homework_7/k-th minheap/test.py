import numpy as np

def tests(get_kth):
    rng = np.random.default_rng(42)
    for _ in range(100):
        k = rng.integers(1, 101)
        arr = rng.random(1000).tolist()
        answer = sorted(arr, reverse=True)[k-1]
        pred = get_kth(arr, k=k)

        assert answer==pred, f'with \nrng = np.random.default_rng(42) (attempt={_}) arr = rng.random(1000)\n got wrong answer'

    assert 1 == get_kth([1], k=1), f'with [1] expected 1 got {get_kth([1], k=1)}'