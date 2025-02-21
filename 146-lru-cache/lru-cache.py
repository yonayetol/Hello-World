class Node:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # HashMap to store key-node pairs
        self.head = Node()  # Dummy head
        self.tail = Node()  # Dummy tail
        self.head.next = self.tail  # Connect head to tail
        self.tail.prev = self.head  # Tail's prev points to head

    def _remove(self, node: Node):
        # Remove node from the linked list
        prev_node = self.head
        while prev_node.next and prev_node.next != node:
            prev_node = prev_node.next
        if prev_node.next:
            prev_node.next = node.next
            if node.next:  # Update next node's previous pointer
                node.next.prev = prev_node

    def _add_to_tail(self, node: Node):
        # Add node to the end of the linked list
        prev_node = self.tail.prev
        prev_node.next = node
        node.prev = prev_node
        node.next = self.tail
        self.tail.prev = node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1  # Key not found
        node = self.cache[key]
        self._remove(node)  # Move accessed node to the tail
        self._add_to_tail(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)  # Evict the node
            node.val = value  # Update value
            self._add_to_tail(node)  # Move to tail
        else:
            if len(self.cache) >= self.capacity:
                lru_node = self.head.next
                self._remove(lru_node)
                del self.cache[lru_node.key]  # Remove from cache
            new_node = Node(key, value)
            self.cache[key] = new_node  # Add to cache
            self._add_to_tail(new_node)  # Add to tail