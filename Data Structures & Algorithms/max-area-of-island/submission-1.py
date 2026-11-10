from collections import deque
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0 
        n, m = len(grid), len(grid[-1])
        seen = set()
        def bfs(sr, sc):
            area = 1
            queue = deque([(sr, sc)])
            seen.add((sr, sc))
            dir =[(-1,0),(1,0),(0,-1),(0,1)]
            while queue:
                r,c = queue.popleft()
                for dr,dc in dir:
                    nr, nc = r+dr, c+dc
                    if 0 <= nr < n and 0 <= nc < m and (nr, nc) not in seen:
                        if grid[nr][nc] == 1:
                            seen.add((nr,nc))
                            queue.append((nr,nc))
                            area += 1
            return area
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1 and grid[i][j] not in seen:
                    max_area = max(max_area, bfs(i,j))
        return max_area
