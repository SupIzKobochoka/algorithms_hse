def tests(lcs):
    answers = {
        ('aaaa', 'bbba'): 'a',
        ('AGGTAB', 'GXTXAYB'): 'GTAB',
        ('ABCBDAB', 'BDCAB'): 'BCAB',
        ('abc', 'abc'): 'abc',
        ('abcdef', 'acf'): 'acf',
        ('abcd', 'xyz'): '',
        ('', 'abcd'): '',
        ('abcd', ''): '',
        ('A', 'A'): 'A',
        ('A', 'B'): '',
    }
    
    for str1, str2 in answers:
        pred = lcs(str1, str2)
        assert pred == answers[(str1, str2)], f'with {str1=} {str2=} got {pred} expected {answers[(str1, str2)]}'