def test(func):
    answers = {
        ((1,), (1,)): True,
        ((1, 2), (2, 1)): True,
        ((2, 1), (1, 2)): True,
        ((1, 1, 2), (1, 2, 1)): True,
        ((1, 1, 2), (2, 1, 1)): True,
        ((1, 1, 3, 2), (2, 1, 1, 3)): False,
        ((1, 2, 3, 4), (2, 4, 1, 3)): False,
        }
    
    for pushed, poped in answers:
        assert func(pushed, poped) == answers[(pushed, poped)], f'With {pushed=}, {poped=} expected {answers[(pushed, poped)]}, got {func(pushed, poped)}'