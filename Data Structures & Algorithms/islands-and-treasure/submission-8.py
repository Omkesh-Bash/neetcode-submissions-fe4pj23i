class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m, n = len(grid), len(grid[0])
        directions = ((0, -1), (0, 1), (1, 0), (-1, 0))
        def dfs(r : int, c : int, d : int):
            if not (r >= 0 and r < m and c >= 0 and c < n and grid[r][c] != -1 and grid[r][c] >= d ):
                return
            grid[r][c] = d
            d+=1
            for dr, dc in directions:
                dfs(r + dr, c + dc, d)


        for r in range(m):
            for c in range(n):
                if grid[r][c] == 0:
                    dfs(r, c, 0)