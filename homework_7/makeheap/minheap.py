class MinHeap:
    def __init__(self):
        # в формате (key, value)
        self.arr = []

    def get_children_index(self, index: int):
        return 2 * index + 1, 2 * index + 2
    
    def get_parent_index(self, index):
        return (index-1)//2
    
    def get_min(self):
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

    def extract_min(self):
        if len(self.arr) == 1:
            return self.arr.pop()[1]
        min_value = self.get_min()
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