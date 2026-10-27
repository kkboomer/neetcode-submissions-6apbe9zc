from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row, col = len(grid), len(grid[0])
        visited = set()
        def bfs(sr, sc):
            queue = deque([(sr, sc)])
            dir =[(-1,0),(1,0),(0,-1),(0,1)]
            while queue:
                r,c = queue.popleft()
                for dr,dc in dir:
                    nr, nc = r+dr, c+dc
                    if 0 <= nr < row and 0<= nc < col and (nr, nc) not in visited:
                        if grid[nr][nc] == "1":
                            visited.add((nr,nc))
                            queue.append((nr,nc))
        res = 0
        for i in range(row):
            for j in range(col):
                if (i,j) not in visited and grid[i][j] == "1":
                    bfs(i,j)
                    res+=1
        return res

        