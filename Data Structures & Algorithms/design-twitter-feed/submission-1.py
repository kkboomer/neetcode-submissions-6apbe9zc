import heapq
from collections import defaultdict
class Twitter:

    def __init__(self):
        self.follows = defaultdict(set)
        self.twts = defaultdict(list)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.twts[userId].append((-self.time, tweetId))
        self.time += 1
        
    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        heap = []
        followers = self.follows[userId]
        followers.add(userId)
        for f in followers:
            if self.twts[f]:
                t =(self.twts[f][-1][0], self.twts[f][-1][1], f, len(self.twts[f])-1)
                heap.append(t)
        heapq.heapify(heap)
        while heap and len(res) < 10:
            time, t_id, u, idx = heapq.heappop(heap)
            res.append(t_id)
            if idx > 0:
                t = ((self.twts[u][idx-1][0], self.twts[u][idx-1][1], u, idx-1))    
                heapq.heappush(heap, t)  
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followeeId == followerId:
            return
        if followerId not in self.follows:
            self.follows[followerId] = set([followeeId])
        else:
            self.follows[followerId].add(followeeId)


    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId == followerId:
            return
        if followerId not in self.follows:
            return
        else:
            self.follows[followerId].discard(followeeId)