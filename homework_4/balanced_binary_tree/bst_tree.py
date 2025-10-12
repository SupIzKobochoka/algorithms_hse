class Node:
    def __init__(self, key=None, value=None, left_child: "Node" = None, right_child: "Node" = None):
        self.key = key
        self.value = value
        self.left_child = left_child
        self.right_child = right_child

class BST:
    def __init__(self):
        self.head = None

    def get(self, key):
        def get_node(key, node: Node) -> Node:
            if node is None: raise KeyError('key not found')
            if node.key == key:
                return node
            if node.key > key:
                return get_node(key, node.left_child) 
            return get_node(key, node.right_child)
        return get_node(key, self.head).value
    
    def add(self, key, value):
        node_to_add = Node(key, value)

        if self.head is None:
            self.head = node_to_add
            return
    
        def get_node_for_value(start_node: Node):
            if start_node.key > key:
                if start_node.left_child is None:
                    start_node.left_child = node_to_add
                    return
                return get_node_for_value(start_node.left_child)
            elif start_node.key < key:
                if start_node.right_child is None:
                    start_node.right_child = node_to_add
                    return
                return get_node_for_value(start_node.right_child)
            start_node.value = node_to_add.value
            return 
        return get_node_for_value(self.head)
    
    def pop(self, key):
        '''
        ╔════════════════════╗
        ╬░░░░░░░░░░░░░░░░░░░░╬
        ╬░░░░░░░▄█████░░░░░░░╬
        ╬░░░░░░░█───██░░░░░░░╬
        ╬░░░░░░░█───██░░░░░░░╬
        ╬░░░░░░░█───██▄▄▄▄▄▄░╬
        ╬░█▀▀▀▀▀▀───▀▀▀▀▀▀██░╬
        ╬░█──22─if─else───█▀░╬
        ╬░▀▀▀▀▀▀█───██▀▀▀▀░░░╬
        ╬░░░░░░░█───██░░░░░░░╬
        ╬░░░░░░░█───██░░░░░░░╬
        ╬░░░░░░░█───██░░░░░░░╬
        ╬░░░░░░░█───██░░░░░░░╬
        ╬░░░░░░░█───██░░░░░░░╬
        ╬░░░░░░░█───██░░░░░░░╬
        ╬░░░░░░░█▄▄▄▀░░░░░░░░╬
        ╬░░░░░░░░░░░░░░░░░░░░╬
        ╚════════════════════╝
        '''
        def get_node_and_parent(key, child: Node, parent: Node) -> Node:
            if child is None: raise KeyError('key not found')
            if child.key == key:
                return child, parent
            if child.key > key:
                return get_node_and_parent(key, child.left_child, child) 
            return get_node_and_parent(key, child.right_child, child)
        
        child, parent = get_node_and_parent(key, self.head, None)

        # Когда у child нет потомков
        if child.left_child is None and child.right_child is None:
            if parent is None:
                self.head = None
            elif parent.left_child is child:
                parent.left_child = None
            else:
                parent.right_child = None            
            return child.value
        
        # когда у child left потомок None
        if child.left_child is None:
            if parent is None:
                self.head = child.right_child
            elif parent.left_child is child:
                parent.left_child = child.right_child
            else:
                parent.right_child = child.right_child
            return child.value
        
        # когда у child right потомок None
        if child.right_child is None:
            if parent is None:
                self.head = child.left_child
            elif parent.left_child is child:
                parent.left_child = child.left_child
            else:
                parent.right_child = child.left_child
            return child.value
        
        # Остался вариант, когда у child 2 ребёнка
        # В таком случае просто выносим на верх minmax pop, т.е. leftest of right_child
        
        leftest_child = child.right_child
        leftest_child_parent = child

        # Случай, когда у child.right_child нет левого потомка
        if leftest_child is None:
            if parent is None:
                self.head = leftest_child
            elif parent.left_child is child:
                parent.left_child = leftest_child
            else:
                parent.right_child = leftest_child
            leftest_child.left_child
            return child.value
                
        # "Нормальный" случай, когда все есть
        while leftest_child.left_child is not None:
            leftest_child_parent = leftest_child
            leftest_child = leftest_child.left_child
        
        leftest_child_parent.left_child = leftest_child.right_child
        leftest_child.left_child = child.left_child
        leftest_child.right_child = child.right_child
        
        if parent is None:
            self.head = leftest_child
        elif parent.left_child is child:
            parent.left_child = leftest_child
        else:
            parent.right_child = leftest_child

        return child.value