# 19- https://leetcode.com/problems/remove-nth-node-from-end-of-list/
# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        counter = 1
        node = head
        behind = head
        prev = ListNode()
        while node.next:
            if counter >= n:
                prev = behind
                behind = behind.next
            node = node.next
            counter += 1
        if counter == n:
            return head.next
        prev.next = behind.next
        return head
