class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        cache = {} 
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        def helper(x,y):
            if x == m-1 and y == n-1 and obstacleGrid[x][y] == 0:
                return 1
            elif x < 0 or x >=m or y < 0 or y >= n:
                return 0
            elif (x,y) in cache:
                return cache[(x,y)]
            elif obstacleGrid[x][y] == 1:
                return 0
            res = helper(x+1, y) + helper(x, y+1)
            cache[(x,y)] = res
            return res 
        return helper(0,0)
        