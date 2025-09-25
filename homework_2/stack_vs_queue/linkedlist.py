# Двусвязный список

class Node:
    def __init__(self, value, last: 'Node', next: 'Node'):
        self.last = last
        self.next = next
        self.value = value

class LinkedList:
    def __init__(self):
        self._node_start = Node(None, None, None)
        self._node_end = Node(None, None, None)
        self._node_start.next = self._node_end
        self._node_end.last = self._node_start

    def _connect_nodes(self, node1: Node, node2: Node):
        node1.next = node2
        node2.last = node1

    def _get(self, index: int) -> Node:
        '''
        Возвращает Node, считая вместе с _node_end, _node_start
        '''
        if index >= 0:
            node = self._node_start
            for _ in range(index): 
                if node.next is None: raise IndexError('index out of range')
                node = node.next
        else:
            node = self._node_end
            for _ in range(-index - 1):
                if node.last is None: raise IndexError('index out of range')
                node = node.last
        return node
    
    def get(self, index: int = -1):
        if index >= 0:
            node = self._get(index).next
        else:
            node = self._get(index).last
        if node is None or node is self._node_start or node is self._node_end:
           raise IndexError('index out of range')
        return node.value
        
    def add(self, value, index: int = -1):
        node = Node(value, None, None)
        if index >=0:
            node_before = self._get(index)
            self._connect_nodes(node, node_before.next)
            self._connect_nodes(node_before, node)
        else:
            node_after = self._get(index)
            self._connect_nodes(node_after.last, node)
            self._connect_nodes(node, node_after)
    
    def pop(self, index: int = -1):
        node = self._get(index + (index>=0)*2-1)
        self._connect_nodes(node.last, node.next)
        return node.value


if __name__ == '__main__':
    from linkedlist_tests import test
    
    test(LinkedList)