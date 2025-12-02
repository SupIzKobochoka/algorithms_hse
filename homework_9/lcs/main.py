import numpy as np


def get_indices_in_order(len1: int, len2: int):
    base = 0
    for _ in range(min(len1, len2)):

        for intex1 in range(base, len1):
            yield intex1, base

        for intex2 in range(base+1, len2):
            yield base, intex2
        
        base += 1


def get_lsc_box(str1: int, str2: int) -> np.ndarray:
    box = np.zeros((len(str1)+1, len(str2)+1))

    for int1, int2 in get_indices_in_order(len(str1), len(str2)):
        if str1[int1] == str2[int2]:
            box[int1+1, int2+1] = box[int1, int2] + 1
        else:
            box[int1+1, int2+1] = max(box[int1+1,:].max(), box[:,int2+1].max())
    return box


def find_path(box: np.ndarray, int1: int = None, int2: int = None, last_path: list = None) -> list[int]:
    if int1 is None or int2 is None or last_path is None:
        int1, int2 = box.shape
        int1 -= 1
        int2 -= 1
        last_path = list()
    
    current_val = box[int1, int2]
    if current_val == 0:
        return last_path
    
    if box[int1-1, int2] == current_val:
        return find_path(box, int1-1, int2, last_path)
    
    if box[int1, int2-1] == current_val:
        return find_path(box, int1, int2-1, last_path)
    
    last_path.append(int1-1)
    return find_path(box, int1-1, int2-1, last_path)
    

def lcs(str1: str, str2: str) -> str:
    box = get_lsc_box(str1, str2)
    path = find_path(box)
    result = []
    for ind1 in path[::-1]:
        result.append(str1[ind1])

    return ''.join(result)


if __name__ == '__main__':
    from test import tests

    tests(lcs)