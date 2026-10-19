class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [1] * n
        suffix = [1] * n 
        for i in range(1, n):
            prefix[i] = prefix[i-1] * nums[i-1]
        for i in range(1, n):
            suffix[i] = suffix[i-1] * nums[n-i]
        res = []
        for j in range(n):
            res.append(prefix[j]*suffix[n-j-1])
        return res