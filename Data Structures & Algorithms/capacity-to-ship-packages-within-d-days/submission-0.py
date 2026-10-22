class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        def check(m):
            local, day= 0, 0
            for x in weights:
                if local + x > m:
                    day += 1
                    local = 0 
                if day >= days:
                    return False
                local += x 
            return True
        l, h = max(weights), sum(weights)
        res = h
        while l <= h:
            m = (l+h) // 2
            if check(m):
                res = min(res, m)
                h = m-1
            else:
                l = m+1
        return res