class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        if len(intervals) == 1:
            return intervals
        intervals.sort()
        res.append(intervals[0])
        for i in range(1, len(intervals)):
            if intervals[i][0] <= res[-1][1]:
                oldinterval = res.pop()
                lower = min(oldinterval[0], intervals[i][0])
                high = max(oldinterval[1], intervals[i][1])
                res.append([lower, high])
            else:
                res.append(intervals[i])
        return res
            