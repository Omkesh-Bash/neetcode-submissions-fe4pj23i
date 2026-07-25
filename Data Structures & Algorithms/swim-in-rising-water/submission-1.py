
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        adj_list = defaultdict(list)

        def add_to_grid(i, j):
            for di, dj in ((0,1), (1, 0), (-1,0), (0, -1)):
                di += i
                dj += j
                if 0 <= di < n and 0 <= dj < n :
                    adj_list[(i,j)].append((di, dj))

        for i in range(n):
            for j in range(n):
                add_to_grid(i, j)
                
        relaxed = set()
        res = 0
        min_heap = [(grid[0][0], 0, 0)] # cost, x, y
        while True:
            cost, x, y = heapq.heappop(min_heap)
            # print(cost, x, y)
            if (x, y) in relaxed:
                continue
            res = max(res, cost)
            if x == n-1 and y == n-1:
                return res
            relaxed.add((x, y))
            for nx, ny in adj_list[(x, y)]:
                if (nx, ny) not in relaxed:
                    n_cost = max(cost, grid[nx][ny])
                    heapq.heappush(min_heap, (n_cost, nx, ny))