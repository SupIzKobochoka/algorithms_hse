class MyDict:
    def __init__(self):
        '''
        В arr будет храниться пара ключ-значение
        При коллизии будет в первую непустую ячейку класться 
        '''
        self.arr_max_len = 10
        self.arr = [[None, None] for _ in range(self.arr_max_len)]
        self.keys = set()
        self.filled_share_for_resize = 1/2
        self.resize_size_scale = 2

    def _find_key(self, key, index: int) -> int:
        '''
        Идёт по self.arr от index до тех пор пока не найдет key
        Возвращает index найденного значения
        Нет защиты от бесконечного while
        '''
        while self.arr[index][0] != key:
            if index+1 >= self.arr_max_len:
                index=0
            else:
                index += 1
        return index

    def _get_index(self, key, arr_max_len=None) -> int:
        '''
        Возвращает index, посчитанный через hash
        Не учитывает коллизию
        '''
        if arr_max_len is None: 
            arr_max_len = self.arr_max_len
        return hash(key) % arr_max_len

    def _resize(self, new_size: int):
        arr = [[None, None] for _ in range(new_size)]
        for key in self.keys:
            index_old = self._get_index(key)
            index_old = self._find_key(key, index_old)
            value = self.arr[index_old][1]

            index = self._get_index(key, new_size)
            while arr[index][0] is not None:
                if index+1 >= new_size:
                    index = 0
                else:
                    index += 1
            arr[index] = [key, value]
        self.arr = arr
        self.arr_max_len = new_size

    def _check_size(self):
        if len(self.keys) >= self.arr_max_len * self.filled_share_for_resize:
            self._resize(int(self.arr_max_len * self.resize_size_scale))

    def __getitem__(self, key):
        '''
        mydict[key]
        '''
        if key not in self.keys:
            raise KeyError(f'{key} not in keys')
        index = self._get_index(key)
        index = self._find_key(key, index)
        return self.arr[index][1]
    
    def __setitem__(self, key, value):
        '''
        mydict[key] = value
        '''
        index = self._get_index(key)
        if key in self.keys:
            index = self._find_key(key, index)
        else:
            index = self._find_key(None, index)
            self.keys.add(key)
        self.arr[index] = [key, value]
        self._check_size()

    def __delitem__(self, key):
        '''
        del mydict[key]
        '''
        if key not in self.keys:
            raise KeyError(f'{key} not in keys')
        index = self._get_index(key)
        index = self._find_key(key, index)
        self.keys.remove(key)
        self.arr[index] = [None, None]


if __name__ == '__main__':
    from hash_table_test import test

    test(MyDict)