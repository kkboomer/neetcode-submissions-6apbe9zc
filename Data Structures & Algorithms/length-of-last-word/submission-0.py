class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        a = s.split()
        print(a)
        return len(a[-1])