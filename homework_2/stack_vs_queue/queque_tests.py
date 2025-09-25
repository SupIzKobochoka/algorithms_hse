def test(Queque):
    '''
    Проверяю на:
        Правильность push значений
        Наличие ошибки при pop пустого
    '''
    stack = Queque()
    for num in range(10):
        stack.push(num)
    for num_expected in range(10):
        res = stack.pop()
        assert num_expected==res, f'with push [0..9] expected {num_expected}, got {res}'

    stack = Queque()
    try:
        res = stack.pop()
        raise IndexError(f'with .pop() on empty stack expected error, got {res}')
    except:
        ...
    
    
        
    