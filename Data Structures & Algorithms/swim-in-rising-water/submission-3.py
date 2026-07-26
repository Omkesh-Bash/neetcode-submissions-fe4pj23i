class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        directions = ((0, 1), (0, -1), (-1, 0), (1, 0))
        min_heap = [(grid[0][0], 0, 0)]
        visited = [[False]*n for _ in range(n)]
        visited[0][0] = True
        while min_heap:
            cost, x, y = heapq.heappop(min_heap)
            if x == n-1 and y == n-1:
                return cost
            for nx, ny in directions:
                nx += x
                ny += y
                if 0 <= ny < n and 0 <= nx < n and  not visited[nx][ny]:
                    visited[nx][ny] = True
                    heapq.heappush(min_heap, (max(cost, grid[nx][ny]), nx, ny))  