# Complexity:
# Time: O(N+M): Let N and M be length of list1 and list2
# Space: O(1)

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        start = list3 = ListNode(0)
        while list1 is not None and list2 is not None:
            if list1.val < list2.val:
                list3.next = list1
                list1 = list1.next
            else:
                list3.next = list2
                list2 = list2.next
            list3 = list3.next
        list3.next = list1 or list2
        return start.next


l1 = ListNode()
l2 = ListNode()

solve = Solution()
print(solve.mergeTwoLists(l1, l2))

# Your input
# [1,2,4] & [1,3,4]
# Output
# [1,1,2,3,4,4]
