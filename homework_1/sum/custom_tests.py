def test(func):
    answers = {
        '1': 0,
        '2': 2,
        '0': 0,
        '1 1 1': 2,
        '2 4 8': 14,
        '0 0 0': 0,
        '0 1': 0,
        }
    
    for number in answers:
        assert func(number) == answers[number], f'With {number} expected {answers[number]}, got {func(number)}'