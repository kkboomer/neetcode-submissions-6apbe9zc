class Solution:
    def maxKelements(self, nums: list[int], k: int) -> int:
        heap = [-x for x in sorted(nums, reverse=True)[:k]]
        ans = 0
        for i in range(k):
            max_el = heapq.heappop(heap)
            ans-=max_el
            heapq.heappush(heap, max_el // 3)        
        return ans