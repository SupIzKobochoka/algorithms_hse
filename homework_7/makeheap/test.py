import numpy as np

def tests(makeheap1, makeheap2):
    rng = rng = np.random.default_rng(42)
    for _ in range(100):
        arr1 = rng.random([100, 2]).tolist()
        arr2 = arr1.copy()
        
        makeheap1_arr = makeheap1(arr1)[0].arr
        makeheap2_arr = makeheap2(arr2)[0].arr

        def get_children_index(index: int):
            return 2 * index + 1, 2 * index + 2

        def check_arr_heap(arr: list[list], index: int = 0, parent_key=float('-inf')):
            assert parent_key is None or parent_key <= arr[index][0], f'got {parent_key=} and child_key={arr[index][0]}'

            child_left_index, child_right_index = get_children_index(index)
            if len(arr) > child_left_index:
                check_arr_heap(arr, child_left_index, arr[index][0])

            if len(arr) > child_right_index:
                check_arr_heap(arr, child_right_index, arr[index][0])

        check_arr_heap(makeheap1_arr)
        check_arr_heap(makeheap2_arr)