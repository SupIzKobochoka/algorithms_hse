def test(func):
    answers = {
        123: False,
        123321: True,
        1: True,
        0: True,
        11211: True,
        111211: False,
        10001: True
        }
    
    for number in answers:
        assert func(number) == answers[number], f'With {number} expected {answers[number]}, got {func(number)}'