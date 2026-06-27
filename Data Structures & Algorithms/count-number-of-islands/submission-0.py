class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        visited = [["0"]*n for _ in range(m)]
        count = 0

        def _IslandVisiter(i : int , j : int) -> None:
            if((i>=0 and i<m) and (j>=0 and j<n) and visited[i][j] != "1" and grid[i][j] == "1" ):
                visited[i][j] = "1"
                _IslandVisiter(i+1, j)
                _IslandVisiter(i-1, j)
                _IslandVisiter(i, j+1)
                _IslandVisiter(i, j-1)

            

        for i in range(m):
            for j in range(n):
                if(visited[i][j] != "1" and grid[i][j] == "1"):
                    count += 1
                    _IslandVisiter(i, j)
        return count