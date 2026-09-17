class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        mappings = {}
        s = s.split() # s is now a list we can iterate through
        i = 0
        # ok so the lists can be different lengths
        if len(s) != len(pattern):
            return False
        for c in pattern:
            if c not in mappings:
                if s[i] in mappings.values():
                    return False
                mappings[c] = s[i]
            elif mappings[c] != s[i]:
                return False
            i += 1
        return True