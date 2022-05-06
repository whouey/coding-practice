#
# @lc app=leetcode id=110 lang=python3
#
# [110] Balanced Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        if root.left:
            if not self.isBalanced(root.left):
                return False
            else:
                l = self.maxDepth(root.left)
        else:
            l = 0

        if root.right:
            if not self.isBalanced(root.right):
                return False
            else:
                r = self.maxDepth(root.right)
        else:
            r = 0

        return abs(l - r) <= 1

    def maxDepth(self, root):
        if not root:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
# @lc code=end

