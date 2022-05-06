#
# @lc app=leetcode id=111 lang=python3
#
# [111] Minimum Depth of Binary Tree
#

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# @lc code=start
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        l = self.minDepth(root.left)
        r = self.minDepth(root.right)

        if l == 0 or r == 0:
            return l + r + 1
        else:
            return min(l, r) + 1

# @lc code=end

