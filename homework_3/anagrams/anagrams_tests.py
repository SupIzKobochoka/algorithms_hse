def test(funk):
    answers = {
    ("eat","tea","tan","ate","nat","bat"): (("bat"), ("nat","tan"), ("ate","eat","tea")),
    ('aaa', 'aaab', 'baaa'): (('aaa'), ('aaab', 'baaa')),
    ('aaa', 'aaab'): (('aaa'), ('aaab')),
    ('aaa'): (('aaa')),

    }
    for words in answers:
        res = funk(list(words))
        res_set = list(map(set, res))
        for ans_i in answers[words]:
            assert (set(ans_i) in res_set), f'for {words} got {res}, except {answers[words]}'
            