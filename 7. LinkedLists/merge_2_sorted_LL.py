# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        newList = ListNode()
        curMin = newList

        while list1 and list2:
            if list1.val > list2.val:
                curMin.next = list2
                list2 = list2.next
                curMin = curMin.next
            else:
                curMin.next = list1
                list1 = list1.next
                curMin = curMin.next
        # at this point one of them has terminated and we'll need to join the rest
        curMin.next = list1 if list1 else list2
        return newList.next
