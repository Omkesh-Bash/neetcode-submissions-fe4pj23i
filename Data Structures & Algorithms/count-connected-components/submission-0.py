
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        unvisited = set([i for i in range(n)])
        adjList = [[] for _ in range(n)]
        for u,v in edges:
            adjList[u].append(v)
            adjList[v].append(u)

        def dfs(u : int):
            if u not in unvisited:
                return
            unvisited.remove(u)
            for v in adjList[u]:
                dfs(v)
        res = 0
        while unvisited:
            dfs(next(iter(unvisited)))
            res += 1

        return res