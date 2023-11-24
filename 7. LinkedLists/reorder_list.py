# 143 https://leetcode.com/problems/reorder-list/


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from typing import Optional


class Solution:
    """
    simple solution would be to add each node to an array and use two pointers. One from the left and another from the right but that takes O(n) memory.
    This solution is to. divide the list into two separate lists, reversing the second list and then merging both lists starting from the first half
    """

    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # find halway point of the list
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        list1 = head
        list2 = slow.next
        slow.next = None  # making the end of first list point none

        # reverse second list
        prev = None
        node = list2
        while node:
            temp = node.next
            node.next = prev
            prev = node
            node = temp
        list2 = prev
        boss = list1
        # merge both lists
        while list2:
            temp1 = list1.next
            temp2 = list2.next
            list1.next = list2
            list2.next = temp1
            list1 = temp1
            list2 = temp2
