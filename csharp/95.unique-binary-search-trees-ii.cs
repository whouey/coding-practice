/*
 * @lc app=leetcode id=95 lang=csharp
 *
 * [95] Unique Binary Search Trees II
 */
 using System.Linq;
 using System.Collections;
 using System.Collections.Generic;

// @lc code=start
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
public class Solution {
    public IList<TreeNode> GenerateTrees(int n) {
        return BuildBSTs(Enumerable.Range(1,n).ToArray()).ToList();
    }

    private IEnumerable<TreeNode> BuildBSTs (int[] values) {
        if (values.Length == 0)
            yield return null;
        else if (values.Length == 1)
            yield return new TreeNode(values[0]);
        else {
            for (int i = 0; i < values.Length; i++) {
                foreach(var left in BuildBSTs(values.Take(i).ToArray()))
                    foreach(var right in BuildBSTs(values.Skip(i+1).Take(values.Length-(i+1)).ToArray()))
                        yield return new TreeNode(values[i], left, right);
            }
        }
    }
}
// @lc code=end

