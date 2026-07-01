
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m, n = len(grid), len(grid[0])
        q = deque()
        visited = [[0]*n for _ in range(m)]
        d = 1

        def add_to_queue(r, c):
            if r >= 0 and r < m and c >= 0 and c < n and visited[r][c] != 1:
                q.append((r, c))
                grid[r][c] = d
                visited[r][c] = 1


        for r in range(m):
            for c in range(n):
                if  grid[r][c] == 0:
                    q.append((r, c))
                    visited[r][c] = 1
                elif grid[r][c] == -1:
                    visited[r][c] = 1

        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                add_to_queue(r-1, c)                
                add_to_queue(r+1, c)                
                add_to_queue(r, c-1)                
                add_to_queue(r, c+1)      
            d+=1 
