#
# @lc app=leetcode id=142 lang=python3
#
# [142] Linked List Cycle II
#

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# @lc code=start
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        try:
            slow, fast = head.next, head.next.next

            while slow != fast:
                slow = slow.next
                fast = fast.next.next

            fast = head

            while slow != fast:
                slow = slow.next
                fast = fast.next

            return slow

        except AttributeError:
            return None
        
# @lc code=end

