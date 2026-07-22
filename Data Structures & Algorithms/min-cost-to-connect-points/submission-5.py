class DisjointSet:
    def __init__(self, size : int):
        self.parent = [i for i in range(size+1)]
        self.size = [1]* (size + 1)
    
    def ultimate_parent(self, node : int) -> int:
        if node == self.parent[node]:
            return node
        self.parent[node] = self.ultimate_parent(self.parent[node])
        return self.parent[node]
    
    def union_by_size(self, u : int, v : int):
        par_u, par_v = self.ultimate_parent(u), self.ultimate_parent(v)
        if par_u == par_v: return False
        if self.size[par_u] > self.size[par_v]:
            self.parent[par_v] = par_u
            self.size[par_u] += self.size[par_v]
        else:
            self.parent[par_u] = par_v
            self.size[par_v] += self.size[par_u]
        return True



class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        X, Y = 0, 1

        min_heap = []
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                cost = abs(points[i][X] - points[j][X]) + abs(points[i][Y] - points[j][Y])
                min_heap.append((cost, i, j))

        heapq.heapify(min_heap)
        cost, size  = 0, 1
        dset =  DisjointSet(len(points))
        while size != len(points):
            m_cost, u, v = heapq.heappop(min_heap)
            if not dset.union_by_size(u, v):
                continue
            cost += m_cost
            size += 1
        return cost