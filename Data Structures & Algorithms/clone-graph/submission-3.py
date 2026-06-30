

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        visited = {node}
        nodes_map = {node : Node(node.val)}
        stack = [node]

        while stack:
            curNode = stack.pop()
            
            for adj in curNode.neighbors:
                if adj not in visited:
                    visited.add(adj)
                    nodes_map[adj] = Node(adj.val)
                    stack.append(adj)
                nodes_map[curNode].neighbors.append(nodes_map[adj]) 
        return nodes_map[node] if node else None