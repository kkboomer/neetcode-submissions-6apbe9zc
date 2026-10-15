class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        frew = {0:1}
        count, prefix = 0, 0
        for i in range(len(nums)):
            prefix = nums[i] + prefix
            if prefix - k in frew:
                count += frew[prefix-k]
            if prefix in frew:
                frew[prefix] += 1
            else:
                frew[prefix] = 1
        return count