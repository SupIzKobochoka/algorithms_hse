def tracer(func):
    depth = 0
    id = 0
    texts = []

    def wrapper(*args, **kwargs):
        nonlocal depth, id, texts
        if depth == 0:
            id = 0
            texts = []  
        current_id = id
        id += 1

        str_args = ', '.join(map(lambda x: x.__repr__(), args))
        str_kwargs = ', '.join([f'{i}={kwargs[i]}' for i in kwargs])
        if len(str_kwargs) > 0:
            str_kwargs = ', ' + str_kwargs
        texts.append([f"{'  ' * depth}{func.__name__}({str_args}{str_kwargs})="])

        depth += 1
        res = func(*args, **kwargs)
        depth -= 1
        texts[current_id].append(res)

        if depth == 0: # т.е. когда вся рекурсия пройдена
            # for text_part_1, text_part_2 in texts:
            #     print(text_part_1, text_part_2, sep='')
            return res, '\n'.join([f'{text_part_1}{text_part_2}' for text_part_1, text_part_2 in texts])
        
        return res
    return wrapper