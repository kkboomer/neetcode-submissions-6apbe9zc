from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        p = {i : [] for i in range(numCourses)}
        idA = [0] * numCourses
        for pr in prerequisites:
            d, s = pr
            if d not in p[s]:
                p[s].append(d)
                idA[d] += 1
        queue = deque([i for i in range(numCourses) if idA[i] == 0])
        order = []
        # we add our courses we "take" here
        while queue:
            node = queue.popleft()
            order.append(node)
            for n in p[node]:
                idA[n] -= 1
                #only add to the queue if all neighbeors are cool
                if idA[n] == 0:
                    queue.append(n)
        return True if len(order) == numCourses  else False
                

