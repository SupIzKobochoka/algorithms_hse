from bst_tree import Node, BST

def test(balanced_binary_tree):
    # Попросил бота написать тест для удобства
    tests = [
        ("""
        5
       / \\
      3   7
     / \\ / \\
    2  4 6  8
        """,
         Node(5, 5,
              Node(3, 3,
                   Node(2, 2),
                   Node(4, 4)),
              Node(7, 7,
                   Node(6, 6),
                   Node(8, 8))),
         True),

        ("""
        1
         \\
          2
           \\
            3
        """,
         Node(1, 1,
              None,
              Node(2, 2,
                   None,
                   Node(3, 3))),
         False),

        ("""
          1
         / \\
        2   3
       /
      4
        """,
         Node(1, 1,
              Node(2, 2,
                   Node(4, 4)),
              Node(3, 3)),
         True),

        ("""
        10
        /
       5
      /
     2
        """,
         Node(10, 10,
              Node(5, 5,
                   Node(2, 2))),
         False),

        ("""
        42
        """,
         Node(42, 42),
         True),

        ("""
           0
          / \\
        -1   1
        """,
         Node(0, 0,
              Node(-1, -1),
              Node(1, 1)),
         True),

        ("""
             10
            /  \\
           5    15
          / \\
         2   7
              \\
               8
        """,
         Node(10, 10,
              Node(5, 5,
                   Node(2, 2),
                   Node(7, 7,
                        None,
                        Node(8, 8))),
              Node(15, 15)),
         False)
    ]

    for scheme, node, expected in tests:
        tree = BST()
        tree.node = node
        res = balanced_binary_tree(tree)
        assert res == expected, f'\nTree:\n{scheme}\nExpected {expected}, got {res}'
