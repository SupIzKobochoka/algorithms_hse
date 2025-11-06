from utils import makeheap

def get_kth(arr: list, k: int):
    
    arr = [[-i, i] for i in arr]
    heap = makeheap(arr)
    for _ in range(k):
        value = heap.extract_min()
    return value

if __name__ == '__main__':
    from test import tests

    tests(get_kth)

