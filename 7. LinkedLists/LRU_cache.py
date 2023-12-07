# 146- https://leetcode.com/problems/lru-cache

class Node:
    def __init__(self, key, value):
        self.key = key
        self.val = value
        self.next = None
        self.prev = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.left = Node(0, 0)
        self.right = Node(0, 0)  # recently visited
        self.left.next, self.right.prev = self.right, self.left

    def insert(self, key):
        node = self.cache[key]
        prev = self.right.prev
        prev.next = node
        node.next = self.right
        node.prev = prev
        self.right.prev = node

    def remove(self, key):
        node = self.cache[key]
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(key)
            self.insert(key)
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(key)
        self.cache[key] = Node(key, value)
        self.insert(key)
        if len(self.cache) > self.capacity:
            # remove from the list and delete the LRU from hashmap
            lru = self.left.next
            self.remove(lru.key)
            del self.cache[lru.key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
