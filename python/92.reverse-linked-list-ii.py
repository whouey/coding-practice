#
# @lc app=leetcode id=92 lang=python3
#
# [92] Reverse Linked List II
#

# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    @classmethod
    def fromList(cls, list):
        dummy = cls()
        cur = dummy

        for i in list:
            cur.next = cls(i)
            cur = cur.next

        return dummy.next

    def print(self):
        l = [self.val]
        cur = self

        while cur.next:
            cur = cur.next
            l.append(cur.val)

        print(l)


# @lc code=start
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head
        
        dummy = ListNode()
        dummy.next = head
        
        cur = dummy
        
        for i in range(right+1):
            
            if i == left - 1:
                left_node = cur.next
                right_node = left_node.next
                for _ in range(right-left):
                    left_node.next = right_node.next
                    right_node.next = cur.next
                    cur.next = right_node

                    right_node = left_node.next
                break

            cur = cur.next

        return dummy.next

# @lc code=end

Solution().reverseBetween(ListNode.fromList([1,2,3,4,5,6,7]), 1, 4)