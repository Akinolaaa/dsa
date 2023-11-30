# 2- https://leetcode.com/problems/add-two-numbers/description/

from typing import Optional


class ListNode:
    def __init__(self, x: int, next: "ListNode" = None):
        self.val = int(x)
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode()
        cur = dummy

        carry = 0
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            # new digit
            val = v1 + v2 + carry
            carry = val // 10
            val = val % 10
            cur.next = ListNode(val)

            # update ptrs
            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next

    def addTwoNumbers1(
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
