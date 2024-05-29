class Node:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.nex = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.r, self.l = Node(), Node()
        self.l.next = self.r
        self.r.prev = self.l

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.remove(node)
        self.insert(node)
        return node.value
        
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        node = Node(key, value)
        self.insert(node)
        self.cache[key] = node

        if len(self.cache) > self.capacity:
            key = self.l.next.key
            self.l = self.l.next
            del self.cache[key]
    
    def insert(self, node):
        prev = self.r.prev
        prev.next = node
        self.r.prev = node
        node.prev = prev
        node.next = self.r
    
    def remove(self, node):
        prev, nex = node.prev, node.next
        prev.next = nex
        nex.prev = prev


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)