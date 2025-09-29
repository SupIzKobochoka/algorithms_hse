def test(HashTable):
    '''
    Буду проверять на:
        Корректность get_item
        Корректность set_item
        Корректность del_item
        Корректность при коллизии
        Корректность для большого числа значений
    '''
    mydict = HashTable()
    for num in range(1_000):
        mydict[num] = num
    for num in range(1_000):
        assert mydict[num] == num, f'with mydict[0...999]=[0...999] and key={num} expected {num}, got {mydict[num]}'

    for key in range(1000):
        mydict[key] = 1
    for key in range(1000):
        assert mydict[key] == 1, f'with was mydict[0...999]=[0...999] and after mydict[0...999]=0, with {key=} expected 1, got {mydict[key]}'
        
    for key in list(mydict.keys):
        del mydict[key]
        try:
            mydict[key]
            raise IndexError(f'with deleted key mydict[key] return smth')
        except:
            ...
    assert len(mydict.keys)==0, f'with deleted all keys len(mydict.keys) > 0'

    # Заранее знаю, что начальный размер зарезервированный = 10
    # hash(1) % 10 == hash(11) % 10 == hash(21) % 10 == hash(31) % 10

    mydict = HashTable()
    for num in [1, 11, 21, 31]:
        mydict[num] = num
    for num in [1, 11, 21, 31]:
        assert mydict[num] == num, f'with mydict[1, 11, 21, 31]=[1, 11, 21, 31] (has collision), with key={num}, expected {num}, got {mydict[num]}'


