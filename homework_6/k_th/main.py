import sys
sys.setrecursionlimit(100_000_000)

def _partition(li: list, flag_left, flag_right):
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


def quickselect(arr: list, k: int, index_left=None, index_right=None) -> list:
    if len(arr) < k:
        raise IndexError('k > len(arr)')

    if index_left is None or index_right is None:
        index_left = 0
        index_right = len(arr) - 1
        arr = arr.copy()
        k = len(arr) - k  # :)

    split_index = _partition(arr, index_left, index_right)

    if split_index == k:
        return arr[k]
    
    if split_index > k:
        return quickselect(arr, k, index_left, split_index-1)

    else:
        return quickselect(arr, k, split_index+1, index_right)
    

if __name__ == '__main__':
    from test import tests

    tests(quickselect)