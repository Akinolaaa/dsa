# 23- https://leetcode.com/problems/merge-k-sorted-lists/
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: list[Optional[ListNode]]) -> Optional[ListNode]:
        if (not lists) or len(lists) < 1:
            return None

        while len(lists) > 1:
            mergedLists = []

            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if (i + 1 < len(lists)) else None
                l3 = self.mergeLists(l1, l2)
                mergedLists.append(l3)
            lists = mergedLists
        return lists[0]

    def mergeLists(self, l1, l2):
        dummy = ListNode()
        cur = dummy
        i = l1
        j = l2

        while i and j:
            if i.val < j.val:
                cur.next = i
                i = i.next
            else:
                cur.next = j
                j = j.next
            cur = cur.next
        cur.next = i if i else j
        return dummy.next
