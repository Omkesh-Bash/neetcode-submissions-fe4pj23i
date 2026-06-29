
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        visited = set()
        q = deque()
        q.append(node)
        nodes_map = defaultdict(Node)

        while q:
            curNode = q.popleft()
            nodes_map[curNode].val = curNode.val
            for adjNode in curNode.neighbors:
                if adjNode not in visited:
                    visited.add(adjNode)
                    q.append(adjNode)
        
        for curNode in nodes_map.keys():
            for adjNode in curNode.neighbors:
                nodes_map[curNode].neighbors.append(nodes_map[adjNode])
        return nodes_map[node]