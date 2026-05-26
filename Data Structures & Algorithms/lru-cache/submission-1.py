class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        # Dummy nodes
        self.left = Node(0, 0)   # Least Recently Used
        self.right = Node(0, 0)  # Most Recently Used

        self.left.next = self.right
        self.right.prev = self.left

    # Remove node from linked list
    def remove(self, node):
        prev_node = node.prev
        next_node = node.next

        prev_node.next = next_node
        next_node.prev = prev_node

    # Insert node at right side (MRU)
    def insert(self, node):
        prev_right = self.right.prev

        prev_right.next = node
        node.prev = prev_right

        node.next = self.right
        self.right.prev = node

    def get(self, key: int) -> int:

        if key in self.cache:
            node = self.cache[key]

            # Move to MRU position
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

        # Remove LRU node if capacity exceeded
        if len(self.cache) > self.capacity:

            lru = self.left.next

            self.remove(lru)

            del self.cache[lru.key]
            