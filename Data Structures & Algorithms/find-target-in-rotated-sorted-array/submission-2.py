class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        while l <= r:
            m = l+(r-l)//2
            if nums[m] == target:
                return m
            # we find the sorted half to look through, check that first before we look for the value
            if nums[l] <= nums[m]:
                # left side is sorted
                if nums[l] <= target < nums[m]:
                    # on the left side
                    r  = m-1
                else: 
                    # on the right side
                    l = m+1
            else: 
                # right side sorted
                if nums[m] < target <= nums[r]:
                    # on the right side
                    l = m+1
                else: 
                    # on the left side
                    r = m-1
        return -1