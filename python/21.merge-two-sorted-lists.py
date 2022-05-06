#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# @lc code=start
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not (list1 or list2):
            return None

        if list1 and (not list2 or list1.val < list2.val):
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list2.next, list1)
            return list2

# @lc code=end


# class Solution:
#     def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
#         dummy = ListNode()
#         cur = dummy

#         while list1 and list2:
#             if list1.val < list2.val:
#                 cur.next = list1
#                 list1 = list1.next
#                 cur = cur.next
#             else:
#                 cur.next = list2
#                 list2 = list2.next
#                 cur = cur.next

#         if not list1:
#             cur.next = list2
#         elif not list2:
#             cur.next = list1

#         return dummy.next