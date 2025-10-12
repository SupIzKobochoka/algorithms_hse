from bst_tree import BST, Node

# pre-order  NLR
# post-order  LRN
# in-order  LNR
# reverse pre-order
# reverse post-order
# reverse in-order

class tree_search:
    def __init__(self, tree: BST):
        self.tree = tree
    
    def pre_order(self, reverse: bool = False) -> list:
        '''
        NLR
        '''
        values = []
        def get_value(node: Node):
            if not reverse:
                values.append(node.value)
                if node.left_child is not None:
                    get_value(node.left_child)
                if node.right_child is not None:
                    get_value(node.right_child)
            else:
                values.append(node.value)
                if node.right_child is not None:
                    get_value(node.right_child)
                if node.left_child is not None:
                    get_value(node.left_child)
        get_value(self.tree.head)
        return values

    def post_order(self, reverse: bool = False) -> list:
        '''
        LRN
        '''
        values = []
        def get_value(node: Node):
            if not reverse:
                if node.left_child is not None:
                    get_value(node.left_child)
                if node.right_child is not None:
                    get_value(node.right_child)
                values.append(node.value)
            else:
                if node.right_child is not None:
                    get_value(node.right_child)
                if node.left_child is not None:
                    get_value(node.left_child)
                values.append(node.value)
        get_value(self.tree.head)
        return values

    def in_order(self, reverse: bool = False) -> list:
        '''
        LNR
        '''
        values = []
        def get_value(node: Node):
            if not reverse:
                if node.left_child is not None:
                    get_value(node.left_child)
                values.append(node.value)
                if node.right_child is not None:
                    get_value(node.right_child)
            else:
                if node.right_child is not None:
                    get_value(node.right_child)
                values.append(node.value)
                if node.left_child is not None:
                    get_value(node.left_child)

        get_value(self.tree.head)
        return values
    

if __name__ == '__main__':
    from tree_search_tests import test

    test(tree_search)