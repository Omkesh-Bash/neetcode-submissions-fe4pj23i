class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        unvisited = set(range(n))
        adjList = [[] for _ in range(n)]
        for u,v in edges:
            adjList[u].append(v)
            adjList[v].append(u)

        def dfs(u : int):
            unvisited.remove(u)
            for v in adjList[u]:
                if v in unvisited:
                    dfs(v)
        res = 0
        while unvisited:
            dfs(next(iter(unvisited)))
            res += 1

        return res
