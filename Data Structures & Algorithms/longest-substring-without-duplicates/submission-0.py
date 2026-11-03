class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        charS = set()
        start = 0
        for end in range(len(s)):
            while s[end] in charS:
                charS.remove(s[start])
                start += 1
            charS.add(s[end])
            longest = max(longest, end - start + 1)
        return longest