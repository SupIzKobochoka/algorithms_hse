class RollingHash:
    def __init__(self, hash_base: int = 4, hash_mod: int = None):
        self.hash_base = hash_base
        self.hash_mod = hash_mod

    def hash_char(self, char: str) -> int:
        return ord(char)
    
    def hash_string(self, string: str) -> int:
        hash_ = sum(self.hash_char(string[-ind-1]) * self.hash_base ** ind for ind in range(len(string)))
        if self.hash_mod is not None:
            return hash_ % self.hash_mod
        return hash_
    
    def fit_step(self, string: str) -> int:
        self.wind_size = len(string)
        self.current_hash = self.hash_string(string)
        return self.current_hash
    
    def step(self, past_char: str, new_char: str) -> int:
        hash_past = self.hash_char(past_char)
        hash_new = self.hash_char(new_char)
        self.current_hash = (self.current_hash - hash_past * self.hash_base ** (self.wind_size - 1)) * self.hash_base + hash_new
        if self.hash_mod is not None:
            self.current_hash = self.current_hash % self.hash_mod
        return self.current_hash
    

def rabin_karp(string: str, substring: str) -> int|None:
    rh = RollingHash()
    target = rh.hash_string(substring)
    predict = rh.fit_step(string[:len(substring)])
    if target == predict:
        if substring == string[:len(substring)]:
            return 0
    
    for ind in range(len(string) - len(substring)):
        predict = rh.step(past_char=string[ind],
                          new_char=string[ind+len(substring)])
        
        if target == predict:
            if substring == string[ind+1:ind+1+len(substring)]:
                return ind+1
    
if __name__ == '__main__':
    from test import tests

    tests(rabin_karp)
            
