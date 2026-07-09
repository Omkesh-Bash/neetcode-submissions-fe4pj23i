class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        size = [1]*n
        parents = list(range(n))

        def find(u : int) -> int:
            if u == parents[u]:
                return u
            parents[u] = find(parents[u])
            return parents[u]
        
        res = n
        def union(u : int, v : int):
            pu, pv = find(u), find(v)
            if pu == pv: 
                return
            if size[pu] > size[pv]:
                size[pu] += size[pv]
                parents[pv] = pu
            else:
                size[pv] += size[pu]
                parents[pu] = pv
            nonlocal res 
            res -= 1

        for u, v in edges:
            union(u, v)

        return res