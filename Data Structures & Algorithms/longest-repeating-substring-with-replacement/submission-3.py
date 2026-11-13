class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        h = {}
        l = 0
        max_len = 0
        replace = 0
        max_freq = 0
        for r in range(len(s)):
            if s[r] not in h:
                h[s[r]] = 1
            else:
                h[s[r]] += 1
            max_freq = max(max_freq, h[s[r]])
            replace = r - l + 1 - max_freq
            while replace > k:
                h[s[l]] -= 1
                l += 1
                replace = r - l + 1 - max_freq
            max_len = max(max_len, r-l+1)
        return max_len
