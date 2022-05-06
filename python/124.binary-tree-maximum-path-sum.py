#
# @lc app=leetcode id=124 lang=python3
#
# [124] Binary Tree Maximum Path Sum
#

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# @lc code=start
class Solution:
    def __init__(self):
        self.res = 0
    
    def maxPathSum(self, root: TreeNode) -> int:        
        self.res = root.val
        self.dfs(root)
        return self.res
    
    def dfs(self, n: TreeNode) -> int:
        l = self.dfs(n.left) if n.left else 0
        r = self.dfs(n.right) if n.right else 0
        m = max(n.val, l + n.val, r + n.val)
        self.res = max(self.res, m, l + r + n.val)
        return m
# @lc code=end

