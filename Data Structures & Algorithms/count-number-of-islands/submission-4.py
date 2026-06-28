
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        count = 0
        directions = ((0, 1), (1, 0), (-1, 0), (0, -1))

        def bfs(i : int , j : int) -> None:
                grid[i][j] = "0"
                q = deque([(i,j)])
                while q:
                    i, j = q.popleft()
                    for di, dj in directions:
                        di, dj = i + di, j + dj
                        if not (di < 0 or di >= m or dj < 0 or dj >= n or  grid[di][dj] != "1"):
                            grid[di][dj] = "0"
                            q.append((di, dj))




        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    count += 1
                    bfs(i, j)
        
        return count