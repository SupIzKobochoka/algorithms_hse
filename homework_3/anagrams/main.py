def anagrams(strs: list[str]) -> list[list[str]]:
    def get_letter_counter(word: str) -> tuple:
        letter_counter = [0 for _ in range(25)]
        for letter in word:
            letter_counter[ord(letter) - 97] += 1
        return tuple(letter_counter)
    
    letter_counter_set = set()
    letter_counter_word = dict()
    for word in strs:
        letter_counter = get_letter_counter(word)
        if letter_counter in letter_counter_set:
            letter_counter_word[letter_counter].append(word)
        else:
            letter_counter_set.add(letter_counter)
            letter_counter_word[letter_counter] = [word]
    return list(letter_counter_word.values())

if __name__ == '__main__':
    from anagrams_tests import test

    test(anagrams)