# 138- # https://leetcode.com/problems/copy-list-with-random-pointer/
from typing import Optional


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
        
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        store = {}
        node = head

        while node:
            store[node] = Node(node.val)
            node = node.next

        node = head
        while node:
            if(node.next):
                store[node].next = store[node.next]
            if(node.random):
                store[node].random = store[node.random]
            node = node.next
        return store[head] if head else None