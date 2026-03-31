class Node:
    def __init__(self, key: int  = 0, val: int = 0):
        self.key = key
        self.val = val
        self.prev = self.next = None    
class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {} # key : node
        self.cap = capacity
        self.left, self.right = Node(), Node()
        self.left.next, self.right.prev = self.right, self.left

    def remove(self, node: Node) -> Node:
        node.prev.next, node.next.prev = node.next, node.prev
        return node

    def insert(self, node: Node):
        self.right.prev.next, self.right.prev, node.prev, node.next = node, node, self.right.prev, self.right 

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.remove(self.cache[key])
            self.insert(node)
            # self.cache[key] = node
            return self.cache[key].val
        return -1
            

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        node = Node(key, value)
        self.insert(node)
        self.cache[key] = node

        if len(self.cache) > self.cap:
            node = self.remove(self.left.next)
            del self.cache[node.key]

        