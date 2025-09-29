def two_sum(arr: list[int], k: int) -> str:
    # Предполагаю, что 2 различных индекса нужно найти
    arr_set = set()
    num_index = dict()
    for index, num in enumerate(arr):
        target = k - num
        if target in arr_set:
            return f'{num_index[target]} {index}'
        else:
            arr_set.add(num)
            num_index[num] = index

if __name__ == '__main__':
    from two_sum_tests import test

    test(two_sum)