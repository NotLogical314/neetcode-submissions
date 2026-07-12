class Node:
    def __init__(self,key , value):
        self.key = key
        self.value = value
        self.previous = None
        self.next = None
        
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.left = Node(0 , 0)
        self.right = Node(0 , 0)
        self.right.prev = self.left
        self.left.next = self.right

    def remove(self ,  node):
        prev_node = node.prev
        next_node = node.next

        prev_node.next = next_node
        next_node.prev = prev_node

    def insert(self, node):
        prev_right = self.right.prev

        prev_right.next = node
        node.prev = prev_right

        node.next = self.right
        self.right.prev = node
        
    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]

            self.remove(node)
            self.insert(node)

            return node.value

        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])

        node = Node(key, value)

        self.cache[key] = node
        self.insert(node)

        if len(self.cache) > self.capacity:

            lru = self.left.next

            self.remove(lru)

            del self.cache[lru.key]
