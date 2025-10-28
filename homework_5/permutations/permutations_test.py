from itertools import permutations as permutations_perfect

def tests(permutations):
    arrs = [[1,], [1, 2], [1, 2, 3], [1, 1, 1], [1, 1, 2, 2]]

    for arr in arrs:
        answer = set(permutations_perfect(arr))
        result = set(map(tuple, permutations(arr)[0]))

        assert answer == result, f'with {arr=} expected {answer}, got {result}'
