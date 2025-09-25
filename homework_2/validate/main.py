def validate(pushed: list | tuple, poped: list | tuple) -> bool:
    pushed_gone = []
    poped_index = 0
    for num in pushed:
        if num == poped[poped_index]:
            poped_index += 1
            while len(pushed_gone) != 0 and pushed_gone[-1] == poped[poped_index]:
                pushed_gone.pop()
                poped_index += 1
        else: 
            pushed_gone.append(num)
    return len(pushed_gone) == 0

if __name__ == '__main__':
    from validate_tests import test
    
    test(validate)