from minheap import MinHeap

def makeheap(arr: list[list]|list[tuple]) -> MinHeap:
    arr = arr.copy()
    mh = MinHeap()
    mh.arr = arr

    def shift_down(index, mh):
        index_left, index_right = mh.get_children_index(index)
        child_left_key = mh.arr[index_left][0] if index_left < len(mh.arr) else float('inf')
        child_right_key = mh.arr[index_right][0] if index_right < len(mh.arr) else float('inf')
        if min(child_left_key, child_right_key) < mh.arr[index][0]:
            child_index = min(zip([child_left_key, child_right_key], [index_left, index_right]))[1]
            mh.arr[child_index], mh.arr[index] = mh.arr[index], mh.arr[child_index]
            shift_down(child_index, mh)
        
    for index in range(len(arr)//2)[::-1]:
        shift_down(index, mh)
    return mh