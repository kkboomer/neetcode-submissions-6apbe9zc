from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        freq = [[] for i in range(len(nums))]
        # i = 0 is freq 1, until n-1 is freq n 
        for x in count:
            freq[count[x]-1].append(x)
        res = []
        for i in range(len(freq) - 1 , -1, -1):
            for j in range(len(freq[i])):
                res.append(freq[i][j])
            if len(res) == k:
                break
        return res
        
