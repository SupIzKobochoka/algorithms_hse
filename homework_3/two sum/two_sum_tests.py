def test(funk):
    answers = {
    ((0, 0), 0): '0 1',
    ((1, 2, 3), 3): '0 1',
    ((3, 2, 1), 3): '1 2',
    ((1, 2, 3, 10, 15), 25): '3 4',
    }
    for arr, k in answers:
        res = funk(list(arr), k)
        assert res==answers[(arr, k)], f'{arr=}, {k=} expected {answers[(arr, k)]}, got {res}'