class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        max_1s = 0
        l = 0
        for r in range(len(nums)):
            if nums[r] == 0:
                k -= 1
            if k < 0:
                if nums[l] == 0:
                    k += 1 
                l += 1
            max_1s = max(max_1s, r - l + 1)
        return max_1s