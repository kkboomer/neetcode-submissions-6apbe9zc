class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        cache = {} # -use this bc you cant easlity look through it, use tuples to store the x,y
        def helper(x,y):
            if x == m-1 and y == n-1:
                return 1
            elif x < 0 or x >=m or y < 0 or y >= n:
                return 0
            elif (x,y) in cache:
                return cache[(x,y)]
            res = helper(x+1, y) + helper(x, y+1)
            cache[(x,y)] = res
            return res 
        return helper(0,0)
        