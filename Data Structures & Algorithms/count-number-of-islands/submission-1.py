
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        count = 0
        directions = ((0, 1), (1, 0), (-1, 0), (0, -1))

        def bfs(i : int , j : int) -> None:
            if i >= 0 and i < m and j >= 0 and j < n and grid[i][j] == "1":
                grid[i][j] = "0"
                for di, dj in directions:
                    bfs(di + i, dj + j)

        for i in range(m):
            for j in range(n):
                if(grid[i][j] == "1"):
                    count += 1
                    bfs(i, j)
        
        return count