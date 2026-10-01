class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0
        count, left, product = 0, 0, 1
        for i in range(len(nums)):
            product *= nums[i]
            while product >= k and left <= i:
                product //= nums[left]
                left+=1
            count += (i - left + 1)
        return count