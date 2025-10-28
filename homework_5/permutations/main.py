from tracer import tracer

@tracer
def permutations(arr: list, fixed_part: list = []) -> list[list]:
    if len(arr) == 1:
        return [fixed_part + arr] 
    
    perms = []
    for index in range(len(arr)):
        res = permutations(arr[:index] + arr[index+1:], fixed_part=fixed_part + [arr[index]])
        perms.extend(res)

    return perms

if __name__ == '__main__':
    from permutations_test import tests

    tests(permutations)