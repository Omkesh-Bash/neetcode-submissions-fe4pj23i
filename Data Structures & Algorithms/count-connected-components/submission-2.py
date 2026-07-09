class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        ranks = [1]*n
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
            if ranks[pu] > ranks[pv]:
                ranks[pu] += ranks[pv]
                parents[pv] = pu
            else:
                ranks[pv] += ranks[pu]
                parents[pu] = pv
            nonlocal res 
            res -= 1

        for u, v in edges:
            union(u, v)

        return res