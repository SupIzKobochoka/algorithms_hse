from bst_tree import BST

def test(tree_search):
    tests = [
        # сбалансированное
        ([5, 3, 7, 2, 4, 6, 8], {
            ('pre', False): ['5', '3', '2', '4', '7', '6', '8'],
            ('pre', True):  ['5', '7', '8', '6', '3', '4', '2'],
            ('post', False): ['2', '4', '3', '6', '8', '7', '5'],
            ('post', True):  ['8', '6', '7', '4', '2', '3', '5'],
            ('in', False): ['2', '3', '4', '5', '6', '7', '8'],
            ('in', True):  ['8', '7', '6', '5', '4', '3', '2'],
        }),
        # все правые потомки
        ([1, 2, 3, 4], {
            ('pre', False): ['1', '2', '3', '4'],
            ('pre', True):  ['1', '2', '3', '4'],
            ('post', False): ['4', '3', '2', '1'],
            ('post', True):  ['4', '3', '2', '1'],
            ('in', False): ['1', '2', '3', '4'],
            ('in', True):  ['4', '3', '2', '1'],
        }),
        # все левые потомки
        ([4, 3, 2, 1], {
            ('pre', False): ['4', '3', '2', '1'],
            ('pre', True):  ['4', '3', '2', '1'],
            ('post', False): ['1', '2', '3', '4'],
            ('post', True):  ['1', '2', '3', '4'],
            ('in', False): ['1', '2', '3', '4'],
            ('in', True):  ['4', '3', '2', '1'],
        })
    ]

    for arr, answers in tests:
        tree = BST()
        for k in arr:
            tree.add(k, str(k))
        search = tree_search(tree)
        for (mode, reverse) in answers:
            if mode == 'pre':
                res = search.pre_order(reverse)
            elif mode == 'post':
                res = search.post_order(reverse)
            elif mode == 'in':
                res = search.in_order(reverse)
            expected = answers[(mode, reverse)]
            assert res == expected, f'{arr=} {mode=} {reverse=} expected {expected}, got {res}'