class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj_list = [[] for _ in range(n)]
        # course_map = [[] * n-1]
        visited = [False] * n
        numVisited = 0
        
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)

        def dfs(node : int, parent: int):
            if visited[node]:
                return False
            visited[node] = True
            nonlocal numVisited
            numVisited+=1
            for v in adj_list[node]:
                if v != parent:
                    if not dfs(v, node):
                        return False
            return True
        
        return dfs(0, -1) and numVisited == n