#
# @lc app=leetcode id=98 lang=python3
#
# [98] Validate Binary Search Tree
#

# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    @classmethod
    def fromList(cls, l):
        if not l:
            return None

        nodes = [cls(l[0])]

        i, cur = 1, 0
        while i < len(l):
            
            if isinstance(l[i], int):
                left = cls(l[i])
                nodes[cur].left = left
                nodes.append(left)
            else:
                nodes.append(None)

            if i+1 < len(l):
                if isinstance(l[i+1], int):
                    right = cls(l[i+1])
                    nodes[cur].right = right
                    nodes.append(right)
                else:
                    nodes.append(None)

            cur += 1
            i += 2

        return nodes[0]

    def print(self):
        nodes = [self]

        cur = 0
        while nodes[cur]:
            nodes.append(nodes[cur].left)
            nodes.append(nodes[cur].right)
            cur += 1
        
        print([x.val if x else None for x in nodes])
        
# @lc code=start
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self._isValidBST(root, None, None)

    def _isValidBST(self, root, min, max):
        if not root: 
            return True

        if isinstance(min, int) and root.val <= min:
            return False
        if isinstance(max, int) and root.val >= max:
            return False

        return self._isValidBST(root.left, min, root.val) and self._isValidBST(root.right, root.val, max)

# @lc code=end

print(Solution().isValidBST(TreeNode.fromList([0, None, -1])))

# class Solution:
#     def isValidBST(self, root: Optional[TreeNode]) -> bool:
#         if not root or (not root.left and not root.right):
#             return True
        
#         if self.isValidBST(root.left) and self.isValidBST(root.right):
#             if (not root.left or self.maxLeaf(root.left) < root.val) \
#                  and (not root.right or root.val < self.minLeaf(root.right)):
#                 return True
            
#         return False
    
#     def maxLeaf(self, root: Optional[TreeNode]) -> int:
#         if root.right:
#             return self.maxLeaf(root.right)
#         return root.val
        
#     def minLeaf(self, root: Optional[TreeNode]) -> int:
#         if root.left:
#             return self.minLeaf(root.left)
#         return root.val

# class Solution:
#     def __init__(self) -> None:
#         self.last = None

#     def isValidBST(self, root: Optional[TreeNode]) -> bool:
#         if not root:
#             return True
        
#         if not self.isValidBST(root.left):
#             return False

#         if self.last and self.last.val >= root.val:
#             return False

#         self.last = root

#         if not self.isValidBST(root.right):
#             return False

#         return True