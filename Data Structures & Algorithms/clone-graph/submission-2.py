
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        visited = set()
        nodes_map = {}

        def dfs(node : Optional['Node']) -> Optional['Node']:
            if node:
                if node not in visited:
                    visited.add(node)
                    nodes_map[node]  = Node(node.val)
                
                for adj in node.neighbors:
                    if adj not in visited:
                        dfs(adj)
                    nodes_map[node].neighbors.append(nodes_map[adj])
        
        dfs(node)
        return nodes_map[node] if node else None