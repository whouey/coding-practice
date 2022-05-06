#
# @lc app=leetcode id=101 lang=python3
#
# [101] Symmetric Tree
#

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# @lc code=start   
from collections import deque


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        q = deque([(root.left, root.right)])

        while q:
            node1, node2 = q.popleft()

            if not node1 and not node2:
                continue
            if not node1 or not node2:
                return False
            if node1.val != node2.val:
                return False

            q.append((node1.left, node2.right))
            q.append((node1.right, node2.left))
        
        return True

# @lc code=end


# class Solution:
#     def isSymmetric(self, root: Optional[TreeNode]) -> bool:
#         if not root:
#             return True
#         return self._isSymm(root.left, root.right)

#     def _isSymm(self, p, q):
#         if not p and not q:
#             return True
#         elif not p or not q:
#             return False
#         else:
#             return p.val == q.val and self._isSymm(p.left, q.right) and self._isSymm(p.right, q.left)
