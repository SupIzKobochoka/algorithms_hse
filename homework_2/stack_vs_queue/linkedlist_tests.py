def test(LinkedListClass):
    '''
    LinkedListClass - Связный список, имеющий методы add, get, pop

    Тесты на:
        Существование методов pop/get/add
        Правильность возвращения и удаления pop
        Правильность возвращения get
        Правильность добавления add
        
        Pop/get/add несуществующих элементов/индексов
        add на несуществующее место

        Правильность работы pop/get/add на краях (index=0, index=-1)
    '''

    # Проверка на существованеи методов
    try:
        linkedlist = LinkedListClass()
        linkedlist.add(0, 0)
        linkedlist.add(0, -1)
        linkedlist.get(0)
        linkedlist.pop(0)
    except Exception as e:
        raise AttributeError(f'error in add/get/pop methods', e)
    
    def get_0to9_linkedlist():
        linkedlist = LinkedListClass()
        for value in range(10):
            linkedlist.add(value, -1)
        return linkedlist

    # Проверка add и get
    linkedlist = get_0to9_linkedlist()
    for get_index in range(10):
        assert linkedlist.get(get_index) == get_index, f'error in add/get, with add [0..9] and get={get_index} expected {get_index}, '\
                                                       f'got {linkedlist.get(get_index)}'
    for get_index in range(10)[::-1]:
        assert linkedlist.get(get_index - 10) == (get_index), f'error in add/get, with add [0..9] and get={get_index - 10} expected {get_index}, '\
                                                       f'got {linkedlist.get(get_index)}'
    
    linkedlist = LinkedListClass()
    try:
        res = linkedlist.get(1)
        raise IndexError(f'.get() out of range index returns {res}, expected Error')
    except:
        ...

    linkedlist = LinkedListClass()
    try:
        res = linkedlist.add(1)
        raise IndexError(f'.add() out of range index returns {res}, expected Error')
    except:
        ...
        
    
    # Проверка на pop
    linkedlist = get_0to9_linkedlist()
    for pop_value_expected in range(10):
        pop_value = linkedlist.pop(0)
        assert pop_value == pop_value_expected, f'error in pop, with add [0..9] expected {pop_value_expected}, '\
                                                f'got {pop_value}'
    linkedlist = get_0to9_linkedlist()
    for pop_value_expected in range(10)[::-1]:
        pop_value = linkedlist.pop(-1)
        assert pop_value == (pop_value_expected), f'error in pop, with add [0..9] expected {pop_value_expected}, '\
                                                f'got {pop_value}'
        
    linkedlist = LinkedListClass()
    linkedlist.add(-1, 0)
    linkedlist.add(-2, 0)
    linkedlist.pop(1)
    try:
        linkedlist.get(1)
        raise IndexError(f'pop dosnt delete element')
    except:
        ...
    
    linkedlist = LinkedListClass()
    try:
        res = linkedlist.get(1)
        raise IndexError(f'.pop() out of range index returns {res}, expected Error')
    except:
        ...
