class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # turn the nums into a set, and then iterate through the set?
        s = set(nums)
        max_c = 0
        count = 0
        for x in s:
            # find start of sequence
            if x - 1 not in s:
                curr = x
                while curr in s:
                    count += 1
                    curr += 1
                max_c = max(count, max_c)
                count = 0
        return max_c