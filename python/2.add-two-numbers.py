#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#

#%%
from typing import Optional

#%%
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

#%%
def list_to_ListNode(l):
    head = None
    cur = None
    for i in range(len(l)):
        node = ListNode(l[i])

        if not head:
            head = node

        if not cur:
            cur = node
        else:
            cur.next = node
            cur = node
    
    return head

def ListNode_to_list(listnode):
    l = []
    cur = listnode
    while cur:
        l.append(cur.val)
        cur = cur.next
    return l

#%%
# @lc code=start
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        answer = ListNode()
        tail = answer
        carry = 0

        while l1 or l2 or carry:
            num1 = l1.val if l1 else 0
            num2 = l2.val if l2 else 0

            carry, out = divmod(num1 + num2 + carry, 10)

            tail.next = ListNode(out)
            tail = tail.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return answer.next
# @lc code=end

#%%
l1 = list_to_ListNode([2, 4, 3])
l2 = list_to_ListNode([5, 6, 4])
answer = ListNode_to_list(Solution().addTwoNumbers(l1, l2))

print(answer)

#%%