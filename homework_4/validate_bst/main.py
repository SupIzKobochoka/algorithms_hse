# Если сделать in-order обход и получим отсортированный список, то бинарное дерево является бинарным деревом поиска
# https://cs.stackexchange.com/questions/95329/if-inorder-traversal-of-a-tree-is-in-ascending-order-will-the-tree-definitely-be
# https://www.baeldung.com/cs/bst-validation

from bst_tree import Node


def validate_bst(node: Node) -> bool:
    # Вместо хранения всего списка, будем проверять больше ли следующее значение предыдущего
    last_value = float('-inf')
    
    def get_value_in_order(node: Node):
        if node.left_child is not None:
            if not get_value_in_order(node.left_child):
                return False

        nonlocal last_value
        if last_value >= node.value:
            return False
        last_value = node.value
        
        if node.right_child is not None:
            if not get_value_in_order(node.right_child):
                return False
            
        return True
    
    return get_value_in_order(node)

if __name__ == '__main__':
    from validate_bst_test import test

    test(validate_bst)

    
    



    

