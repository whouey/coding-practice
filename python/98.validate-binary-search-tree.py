#
# @lc app=leetcode id=98 lang=python3
#
# [98] Validate Binary Search Tree
#

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# @lc code=start
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root or (not root.left and not root.right):
            return True
        
        if self.isValidBST(root.left) and self.isValidBST(root.right):
            if (not root.left or self.maxLeaf(root.left) < root.val) \
                 and (not root.right or root.val < self.minLeaf(root.right)):
                return True
            
        return False
    
    def maxLeaf(self, root: Optional[TreeNode]) -> int:
        if root.right:
            return self.maxLeaf(root.right)
        return root.val
        
    def minLeaf(self, root: Optional[TreeNode]) -> int:
        if root.left:
            return self.minLeaf(root.left)
        return root.val
# @lc code=end

