# 2- https://leetcode.com/problems/add-two-numbers/description/

from typing import Optional


class ListNode:
    def __init__(self, x: int, next: "ListNode" = None):
        self.val = int(x)
        self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        s1 = ""
        s2 = ""
        node = l1
        while node:
            s1 = str(node.val) + s1
            node = node.next
        node = l2
        while node:
            s2 = str(node.val) + s2
            node = node.next
        sol = int(s1) + int(s2)
        sol = str(sol)
        node = None
        for i in sol:
            newNode = ListNode(val=int(i))
            newNode.next = node
            node = newNode
        return node
