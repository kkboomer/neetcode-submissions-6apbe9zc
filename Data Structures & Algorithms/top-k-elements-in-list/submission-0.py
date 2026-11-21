from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for x in nums:
            if x not in count:
                count[x] = 1
            else:
                count[x] += 1
        res = sorted(count.keys(), key= lambda x: -count[x])
        
        return res[:k]
        