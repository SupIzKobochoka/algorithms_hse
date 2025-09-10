def test(func):
    answers = {
        0:0,
        1:0,
        2:0, # 1 не простое 
        3:1,
        4:2,
        6:3,
        10:4,
        11:4,
        }
    
    for number in answers:
        assert func(number) == answers[number], f'With {number} expected {answers[number]}, got {func(number)}'