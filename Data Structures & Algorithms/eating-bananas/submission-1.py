class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def feasible(k: int) -> bool:
            # k is our rate of eating bananas
            hr = 0
            for x in piles:
                if x <= k:
                    hr += 1
                else:
                    hr += (x+k-1) // k
                if hr > h:
                    return False
            return True
        # 1. Define inclusive search boundaries
        left, right = 1, max(piles)
        rate = -1
        while left <= right:
            mid = (left + right) // 2
            # 2. If condition holds, record candidate and search left for an earlier match
            if feasible(mid):
                rate = mid
                right = mid - 1
            # 3. Otherwise, discard the left half
            else:
                left = mid + 1
        return rate
