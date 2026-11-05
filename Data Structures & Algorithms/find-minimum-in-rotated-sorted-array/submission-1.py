class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            m = (l+r) // 2
            # we check if the last item is greater than current, if yes, we found the min
            # else we have to check which side of the pivot we are on by checking against our m
            # if m > r we go right, else left
            # the edge case is if m is 0, then it has to be the minimum
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
        return nums[l]