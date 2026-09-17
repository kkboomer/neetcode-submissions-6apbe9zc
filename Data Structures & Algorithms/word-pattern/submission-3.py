class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        mappings = {}
        s = s.split() # s is now a list we can iterate through
        # ok so the lists can be different lengths
        if len(s) != len(pattern):
            return False
        for c, word in zip(pattern, s):
            if c not in mappings:
                if word in mappings.values():
                    return False
                mappings[c] = word
            elif mappings[c] != word:
                return False
        return True