class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        n+=1
        visited = [False] * n
        visited_count = 0
        adj_list = [[] for _ in range(n)]
        dist = [float('inf')] * n
        dist[k] = 0
        for u, v, w in times:
            adj_list[u].append((v, w))
        pq = [(0, k)]
        res = -1
        while pq:
            weight, u = heapq.heappop(pq)
            if visited[u]:
                continue
            visited[u] = True
            visited_count+=1
            res = max(res, weight)
            for v, w in adj_list[u]:
                if visited[v]:
                    continue
                curr_weight = w + weight
                if dist[v] > curr_weight:
                    dist[v] = curr_weight
                    heapq.heappush(pq, (curr_weight, v))

        return res if visited_count == n-1 else -1 