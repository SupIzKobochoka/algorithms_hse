class Node:
    def __init__(self, value, next: 'Node'):
        self.next = next
        self.value = value

class LinkedListNoDummy:
    def __init__(self):
        self.head = None

    def is_null(self) -> bool:
        return self.head is None

    def _get(self, index: int = 0) -> Node:
        '''
        Возвращает Node
        '''
        if index==0: 
            if self.is_null(): raise IndexError('index out of range')
            return self.head
        
        node = self.head
        for _ in range(index):
            node = node.next
            if node is None: raise IndexError('index out of range')
        return node
    
    def get(self, index: int = 0):
        return self._get(index).value
    
    def add(self, value, index=0):
        if index==0:
            self.head = Node(value, self.head)
        else:
            node_before = self._get(index-1)
            node_before.next = Node(value, node_before.next)
    
    def pop(self, index: int = 0):
        if index==0:
            if self.is_null(): raise IndexError('index out of range')
            value = self.head.value
            self.head = self.head.next
            return value
        
        node_before = self._get(index-1)
        if node_before.next is None: raise IndexError('index out of range')
        value = node_before.next.value
        node_before.next = node_before.next.next
        return value



class LinkedListDummy:
    def __init__(self):
        self.dummy_head = Node(None, None)
        self.dummy_tail = Node(None, None)
        self.dummy_head.next = self.dummy_tail

    def is_null(self) -> bool:
        return self.dummy_head.next is self.dummy_tail

    def _get(self, index: int = 0) -> Node:
        '''
        Возвращает Node считая head
        '''        
        node = self.dummy_head
        for _ in range(index):
            node = node.next
            if node is None or node is self.dummy_tail: raise IndexError('index out of range')
        return node
    
    def get(self, index: int = 0):
        return self._get(index+1).value
    
    def add(self, value, index: int = 0):
        node_before = self._get(index)
        node_before.next = Node(value, node_before.next)
    
    def pop(self, index: int = 0):
        node_before = self._get(index)
        if node_before is self.dummy_tail: raise IndexError('index out of range')
        value = node_before.next.value
        node_before.next = node_before.next.next
        return value

            