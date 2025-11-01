from utils import time_count
import sys
sys.setrecursionlimit(100_000_000)

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


def _partition(li: list, flag_left: int, flag_right: int) -> None:
        if flag_left >= flag_right:
            split_index = min(flag_left, flag_right)
            return split_index 
        
        element_left = li[flag_left]
        support_element = li[flag_right]

        if element_left >= support_element:
            li[flag_left], li[flag_right-1], li[flag_right] = li[flag_right-1], li[flag_right], li[flag_left]
            return _partition(li, flag_left=flag_left, flag_right=flag_right-1)
        
        else:
            return _partition(li, flag_left=flag_left+1, flag_right=flag_right)

@time_count
def quicksort(arr: list, _index_left: int = None, _index_right: int = None) -> list:
    
    if _index_left is None or _index_right is None:
        split_index = _partition(arr, flag_left=0, flag_right=len(arr)-1)
        quicksort(arr, 0, split_index-1)
        quicksort(arr, split_index+1, len(arr)-1)
    
    elif _index_left < _index_right:
        split_index = _partition(arr, _index_left, _index_right)
        quicksort(arr, _index_left, split_index-1)
        quicksort(arr, split_index+1, _index_right)

    if _index_left is None or _index_right is None:
        return arr

@time_count
def mergesort(arr: list, _index_left: int = None, _index_right: int = None) -> list:
    # Честно, я сам не понял, как оно по итогу заработало)))
    flag = False
    if _index_left is None or _index_right is None:
        _index_left = 0
        _index_right = len(arr)
        flag = True
    
    if _index_right - _index_left != 1:
        split_by = (_index_right + _index_left)//2
        mergesort(arr, _index_left, split_by)
        mergesort(arr, split_by, _index_right)
        _merge_sorted(arr, _index_left, split_by,
                           split_by, _index_right)
    
    if flag:
        return arr
 
if __name__ == '__main__':
    from test import tests

    tests(quicksort, mergesort)

