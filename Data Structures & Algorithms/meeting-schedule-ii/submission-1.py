"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start, end = sorted([i.start for i in intervals]), sorted([i.end for i in intervals])
        s,e,c,m =0, 0, 0 ,0
        n = len(intervals)
        while s < n and e < n:
            if start[s] < end[e]:
                c+=1
                s+=1
            else:
                c -= 1
                e +=1
            m = max(m,c)
        return m
