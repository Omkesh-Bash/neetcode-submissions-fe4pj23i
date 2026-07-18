class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        X, Y = 0, 1
        visited = [False]*len(points)
        adj_list = [[] for _ in range(len(points))] # cost, destination_index

        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                cost = abs(points[i][X] - points[j][X]) + abs(points[i][Y] - points[j][Y])
                adj_list[i].append((cost, j))
                adj_list[j].append((cost, i))
        min_heap = [(0, 0)]
        heapq.heapify(min_heap)
        visited_count = 0
        cost = 0
        while visited_count != len(points):
            c, i = heapq.heappop(min_heap)
            if visited[i]:
                continue
            cost += c
            visited[i] = True
            for point in adj_list[i]:
                if not visited[point[1]]:
                    heapq.heappush(min_heap, point)
            visited_count+=1
        return cost
