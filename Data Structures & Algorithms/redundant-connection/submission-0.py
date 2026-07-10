
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = list(range(len(edges)+1))
        size = [1]*(len(edges) + 1)
        
        def find(u : int) -> int:
            if u == parent[u]:
                return u
            parent[u] = find(parent[u])
            return parent[u]
        
        def union(u : int , v : int) -> bool:
            pu, pv = find(u), find(v)
            if pu == pv:
                return True
            if size[pu] > size[pv]:
                size[pu] += size[pv]
                parent[pv] = pu
            else:
                size[pv] += size[pu]
                parent[pu] = pv
            return False
        
        for u, v in edges:
            if union(u, v):
                return [u, v]