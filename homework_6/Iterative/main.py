from utils import time_count

def _partition(li: list, flag_left, flag_right):
        while flag_left < flag_right:
            element_left = li[flag_left]
            support_element = li[flag_right]

            if element_left >= support_element:
                li[flag_left], li[flag_right-1], li[flag_right] = li[flag_right-1], li[flag_right], li[flag_left]
                flag_right -= 1
            else:
                flag_left += 1
        split_index = min(flag_left, flag_right)
        return split_index 

@time_count
def quicksort(arr: list) -> list:
    indexes = [(0, len(arr)-1)]
    while len(indexes) > 0:
        index_left, index_right = indexes.pop()
        if index_left < index_right:
            split_index = _partition(arr, index_left, index_right)
            new_indexes = [(index_left, split_index-1), (split_index+1, index_right)]
            indexes.extend(new_indexes)
    return arr


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

@time_count
def mergesort(arr: list):
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

if __name__ == '__main__': 
    from test import tests

    tests(quicksort, mergesort)


