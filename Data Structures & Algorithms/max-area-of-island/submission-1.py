# Medium
from typing import List
from collections import deque

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        result = 0
        directions = ((0, 1), (1, 0), (-1, 0), (0, -1))

        def bfs(i : int , j : int) -> int:
            grid[i][j] = 0
            count = 1
            q = deque([(i,j)])
            while q:
                i, j = q.popleft()
                for di, dj in directions:
                    di, dj = i + di, j + dj
                    if not (di < 0 or di >= m or dj < 0 or dj >= n or  grid[di][dj] != 1):
                        grid[di][dj] = 0
                        count += 1
                        q.append((di, dj))
            return count



        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    result = max(result,bfs(i, j))
        
        return result
