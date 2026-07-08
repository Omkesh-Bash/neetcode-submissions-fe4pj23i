class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj_list = [[] for _ in range(n)]
        # course_map = [[] * n-1]
        visited = [False] * n
        
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)

        def dfs(node : int, parent: int):
            if visited[node]:
                return False
            visited[node] = True
            for v in adj_list[node]:
                if v != parent:
                    if not dfs(v, node):
                        return False
            return True
        
        if dfs(0, -1):
            for visit in visited:
                if not visit:
                    return False
            return True
        else :
            return False