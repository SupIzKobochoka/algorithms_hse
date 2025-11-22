class MinHeap:
    def __init__(self):
        # в формате (key, value)
        self.arr = []

    def is_empty(self) -> bool:
        return len(self.arr) == 0

    def get_children_index(self, index: int):
        return 2 * index + 1, 2 * index + 2
    
    def get_parent_index(self, index: int):
        return (index-1)//2
    
    def get_min(self, return_with_key: bool = False):
        if return_with_key:
            return self.arr[0]
        return self.arr[0][1]
    
    def insert(self, key, value):
        to_add = (key, value)
        self.arr.append(to_add)

        def shift_up(index):
            parent_index = self.get_parent_index(index)
            if index != 0 and self.arr[parent_index][0] > self.arr[index][0]:
                self.arr[parent_index], self.arr[index] = self.arr[index], self.arr[parent_index]
                return shift_up(parent_index)
            
        shift_up(len(self.arr)-1)

    def extract_min(self, return_with_key=False):
        min_value = self.get_min(return_with_key)
        if len(self.arr) == 1:
            self.arr = []
            return min_value
        
        self.arr[0] = self.arr.pop()

        def shift_down(index):
            index_left, index_right = self.get_children_index(index)
            child_left_key = self.arr[index_left][0] if index_left < len(self.arr) else float('inf')
            child_right_key = self.arr[index_right][0] if index_right < len(self.arr) else float('inf')
            if min(child_left_key, child_right_key) < self.arr[index][0]:
                child_index = min(zip([child_left_key, child_right_key], [index_left, index_right]))[1]
                self.arr[child_index], self.arr[index] = self.arr[index], self.arr[child_index]
                shift_down(child_index)
                
        shift_down(0)
        return min_value

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