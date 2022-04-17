/*
 * @lc app=leetcode id=104 lang=csharp
 *
 * [104] Maximum Depth of Binary Tree
 */

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     public int val;
 *     public TreeNode left;
 *     public TreeNode right;
 *     public TreeNode(int val=0, TreeNode left=null, TreeNode right=null) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

// @lc code=start
public class Solution {
    public int MaxDepth(TreeNode root) {
        if (root == null)
            return 0;
        
        var l = MaxDepth(root.left);
        var r = MaxDepth(root.right);
        
        return (l>r ? l : r) + 1;
    }
}
// @lc code=end

