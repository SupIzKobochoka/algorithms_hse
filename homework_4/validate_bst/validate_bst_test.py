from bst_tree import Node


def test(validate_bst):
    # Попросил бота нарисовать схемы дерева для удобства
    tests = [
        ("""
        5
       / \\
      3   7
     / \\ / \\
    2  4 6   8
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
        5
       /
      9   
        """,
         Node(5, 5,
              Node(9, 9),
              Node(7, 7)),
         False),

        ("""
        10
       / \\
      5   3   
        """,
         Node(10, 10,
              Node(5, 5),
              Node(3, 3)),
         False),

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
         True),

        ("""
        3
         \\
          2
           \\
            1
        """,
         Node(3, 3,
              None,
              Node(2, 2,
                   None,
                   Node(1, 1))),
         False),

        ("""
        42
        """,
         Node(42, 42),
         True),

        ("""
        5
       / \\
      5   6
        """,
         Node(5, 5,
              Node(5, 5),
              Node(6, 6)),
         False),

        ("""
           0
          / \\
       -10   10
       / \\
    -20  -5
        """,
         Node(0, 0,
              Node(-10, -10,
                   Node(-20, -20),
                   Node(-5, -5)),
              Node(10, 10)),
         True),
    ]

    for scheme, node, expected in tests:
        res = validate_bst(node)
        assert res == expected, f'\nTree:\n{scheme}\nExpected {expected}, got {res}'
