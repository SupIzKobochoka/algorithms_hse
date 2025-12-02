def tests(rabin_karp):
    strs = strs = [
        ['aaaa', 'a'],
        ['abcdef', 'cd'],
        ['hello', 'll'],
        ['a' * 100, 'a' * 50],
        ['short', 'sh'],
        ['longerstring', 'string'],
        ['testcase', 'case'],
        ['ababababab', 'baba'],
        ['patternmatching', 'match']
    ]

    for string, substring in strs:
        answer = string.index(substring)
        pred = rabin_karp(string, substring)
        assert answer == pred, f'with {string=} {substring=} got {pred} expected {pred}'

    false_strs = [['fasf', 'zzzzz'], ['afawfafw', 'oooooo'], ['aaaaaefw', 'vvvvvvvv']]
    
    for string, substring in false_strs:
        pred = rabin_karp(string, substring)
        assert pred is None, f'with {string=} {substring=} got {pred} expected None'