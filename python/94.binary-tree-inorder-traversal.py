#
# @lc app=leetcode id=94 lang=python3
#
# [94] Binary Tree Inorder Traversal
#

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# @lc code=start
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        res = []

        cur = root
        while cur or stack:
            while cur:
                stack.append(cur)
                cur=cur.left
            cur = stack.pop()
            res.append(cur.val)
            cur = cur.right
        
        return res
# @lc code=end


# class Solution:
#     def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
#         return list(self._inorder(root))
        
#     def _inorder(self, root):
#         if not root:
#             return
        
#         for i in self._inorder(root.left):
#             yield  i

#         yield root.val

#         for i in self._inorder(root.right):
#             yield  i