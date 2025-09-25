from LinkedList import LinkedListDummy, LinkedListNoDummy, Node

def test(funk, LinkedListClass):

    def array2linked(arr: list|tuple):
        linkedlist = LinkedListClass()
        for value in arr[::-1]:
            linkedlist.add(value)
        return linkedlist
    
    def node2array(node: Node) -> list:
        if node.value==node.next==None:
            return []
        array = []
        while node is not None:
            array.append(node.value)
            node = node.next
        return array
    
    answers = {
    (tuple(), tuple()): [],
    (tuple(), (1,)): [1],
    ((1,2,3), tuple()): [1,2,3],
    ((1,), (1,)): [1, 1],
    ((1,2,3,4), (1,2,3,4)): [1,1,2,2,3,3,4,4],
    ((1,1,), (1,2,3)): [1,1,1,2,3],
    ((1,2,3), (1,1)): [1,1,1,2,3],
    }

    for linkedlist_1_tuple, linkedlist_2_tuple in answers:
        linkedlist_1, linkedlist_2 = array2linked(linkedlist_1_tuple), array2linked(linkedlist_2_tuple)
        res = node2array(funk(linkedlist_1, linkedlist_2))
        assert res==answers[(linkedlist_1_tuple, linkedlist_2_tuple)],\
        f'with {linkedlist_1_tuple, linkedlist_2_tuple} expected {answers[(linkedlist_1_tuple, linkedlist_2_tuple)]}, got {res}'



    
