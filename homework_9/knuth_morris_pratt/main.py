def check_eq_substings(string: str, 
                       index_end: int,
                       step: int
                       ) -> bool:
    for ind in range(step):
        if string[ind] != string[index_end-step+ind+1]:
            return False
    return True


def prefix_f(string: str, current_ind: int = 1, values: list = None) -> list:
    if values is None:
        values = [0]
        if len(string) == 1:
            return [0]
        
    if current_ind == len(string):
        return values
    
    last_value = values[-1]+1
    while last_value != 0:
        if check_eq_substings(string, current_ind, last_value):
            values.append(last_value)
            return prefix_f(string, current_ind+1, values)        
        last_value -= 1
    
    values.append(0)
    return prefix_f(string, current_ind+1, values)


def knuth_morris_pratt(string: str, substring: str, 
                       substring_index: int = 0, string_index: int = 0, prefix: list[int] = None) -> int|None:
    if prefix is None:
        prefix = prefix_f(substring)
    
    if substring_index == len(substring):
        return string_index - substring_index
    
    if string_index == len(string):
        return

    if string[string_index] == substring[substring_index]:
        return knuth_morris_pratt(string, substring,
                                  substring_index+1, string_index+1, prefix)
    
    if substring_index == 0:
        return knuth_morris_pratt(string, substring,
                                  0, string_index+1, prefix)
    
    return knuth_morris_pratt(string, substring,
                              prefix[substring_index], string_index, prefix)

if __name__ == '__main__':
    from test import tests

    tests(knuth_morris_pratt)
            