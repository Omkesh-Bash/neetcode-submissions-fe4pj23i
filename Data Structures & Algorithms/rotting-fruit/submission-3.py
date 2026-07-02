class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        q = deque()
        d = 0
        fresh_fruit_count = 0

        def add_to_queue(r : int, c : int):
            if 0 <= r < m and 0 <= c < n and grid[r][c] == 1:
                nonlocal fresh_fruit_count
                q.append((r, c))
                grid[r][c] = 2
                fresh_fruit_count -= 1

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    fresh_fruit_count += 1
                elif grid[r][c] == 2:
                    q.append((r, c))
                
        while q and fresh_fruit_count > 0:
            for _ in range(len(q)):
                r, c = q.popleft()
                add_to_queue(r-1, c)
                add_to_queue(r+1, c)
                add_to_queue(r, c-1)
                add_to_queue(r, c+1)
            d += 1
        return d if fresh_fruit_count == 0 else -1