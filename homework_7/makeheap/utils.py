import time

def time_count(func):
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        res = func(*args, **kwargs)
        end_time = time.perf_counter()
        return res, end_time - start_time
    return wrapper

def _merge_sorted(arr: list,
                    arr1_left_index: int, arr1_right_index: int, 
                    arr2_left_index: int, arr2_right_index: int,
                    is_single_element: bool = False) -> None:
    # right_index не включительно: [) V [)
    if is_single_element:
        return     
    new_index = []

    left_border = arr1_left_index
    right_border = arr2_right_index

    while arr1_left_index != arr1_right_index and arr2_left_index != arr2_right_index:
        if arr[arr1_left_index] > arr[arr2_left_index]:
            new_index.append(arr2_left_index)
            arr2_left_index += 1
        else:
            new_index.append(arr1_left_index)
            arr1_left_index += 1

    new_index.extend(list(range(arr1_left_index, arr1_right_index)))
    new_index.extend(list(range(arr2_left_index, arr2_right_index)))

    arr_slice_copy = arr[left_border: right_border].copy()
    for number_position, arr_index in enumerate(new_index):
        arr[left_border + number_position] = arr_slice_copy[arr_index - left_border]

def mergesort(arr: list):
    arr = arr.copy()
    indexes = [(i, i+1) for i in range(len(arr))]
    while len(indexes) > 1:
        indexes_new = []
        for window in range(len(indexes)//2):
            index1_left, index1_right = indexes[window*2]
            index2_left, index2_right = indexes[window*2 + 1]
            _merge_sorted(arr, index1_left, index1_right,
                               index2_left, index2_right)
            indexes_new.append((index1_left, index2_right))
        if len(indexes)%2==1:
            indexes_new.append(indexes[-1])
        indexes = indexes_new
    return arr