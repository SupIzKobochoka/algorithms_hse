from LinkedList import LinkedListDummy, LinkedListNoDummy, Node

def merged_list(list_1: LinkedListDummy|LinkedListNoDummy, 
                list_2: LinkedListDummy|LinkedListNoDummy) -> Node:
    node_start = Node(None, None)
    node_next = node_start

    while not list_1.is_null() and not list_2.is_null():
        if list_1.get() < list_2.get():
            node_next.next = Node(list_1.pop(), None)
            node_next = node_next.next
        else:
            node_next.next = Node(list_2.pop(), None)
            node_next = node_next.next
    
    if list_1.is_null():
        while not list_2.is_null():
            node_next.next = Node(list_2.pop(), None)
            node_next = node_next.next
    else:
        while not list_1.is_null():
            node_next.next = Node(list_1.pop(), None)
            node_next = node_next.next
    
    return node_start.next if node_start.next is not None else node_start


if __name__ == '__main__':
    from merged_list_test import test

    test(merged_list, LinkedListDummy)
    test(merged_list, LinkedListNoDummy)
