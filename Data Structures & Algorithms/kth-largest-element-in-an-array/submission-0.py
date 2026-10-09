import heapq
class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        nums = [-n for n in nums]
        h = heapq.heapify(nums)
        for i in range(k-1):
            heapq.heappop(nums)
        return -nums[0]