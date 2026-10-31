from math import floor
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = {}
        n = len(nums)
        for x in nums:
            if x not in count:
                count[x] = 1
            else:
                count[x] += 1
        return [x for x in count if count[x] > floor(n/3)]