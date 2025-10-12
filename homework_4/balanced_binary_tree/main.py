from bst_tree import Node, BST

def balanced_binary_tree(tree: BST) -> bool:
    node = tree.node
    def counter(node: Node):
        if node is None:
            return 0
        
        left_child_count = counter(node.left_child)
        right_child_count = counter(node.right_child)

        if left_child_count is False or right_child_count is False:
            return False
        
        if abs(left_child_count - right_child_count) > 1:
            return False

        return 1 + max(left_child_count, right_child_count)
    
    res = counter(node)
    return False if isinstance(res, bool) else True

if __name__ == '__main__':
    from balanced_binary_tree_test import test

    test(balanced_binary_tree)

