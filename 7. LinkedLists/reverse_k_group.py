# 25- https://leetcode.com/problems/reverse-nodes-in-k-group
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        groupPrev = dummy
        while True:
            kth = self.findkth(groupPrev, k)
            if not kth:
                break
            groupNext = kth.next

            # reverse
            prev, cur = kth.next, groupPrev.next
            tail = cur
            while cur != groupNext:
                temp = cur.next
                cur.next = prev
                prev = cur
                cur = temp
            groupPrev.next = kth
            tail.next = groupNext
            groupPrev = tail
        return dummy.next

    def findkth(self, start, k):
        cur = start
        while cur and k > 0:
            cur = cur.next
            k -= 1
        return cur
