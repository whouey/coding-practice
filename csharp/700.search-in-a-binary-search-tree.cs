/*
 * @lc app=leetcode id=700 lang=csharp
 *
 * [700] Search in a Binary Search Tree
 */
 using System.Collections;
 using System.Collections.Generic;

var root = TreeNode.FromEnumerable(new[] {4,2,7,1,3});
var val = 1;
System.Console.WriteLine(new Solution().SearchBST(root, val));
 
 
// Definition for a binary tree node.
public class TreeNode {
    public int val;
    public TreeNode left;
    public TreeNode right;
    public TreeNode(int val=0, TreeNode left=null, TreeNode right=null) {
        this.val = val;
        this.left = left;
        this.right = right;
    }

    public static TreeNode FromEnumerable(int[] array) {
        if (array.Length == 0)
            return null;

        var root = new TreeNode(array[0]);
        var nodes = new List<TreeNode>() { root };

        int i = 1;
        int cur = 0;
        while (i < array.Length) {

            var left = new TreeNode(array[i]);
            nodes[cur].left = left;
            nodes.Add(left);

            if (i+1 < array.Length) {
                var right = new TreeNode(array[i+1]);
                nodes[cur].right = right;
                nodes.Add(right);
            }
            cur+=1;
            i+=2;
        }

        return root;
    }

    public IEnumerable<int> ToEnumerable() {
        var nodes = new List<TreeNode>() { this };
        var cur = 0;
        while (nodes[cur].left != null || nodes[cur].right != null){
            if (nodes[cur].left != null)
                nodes.Add(nodes[cur].left);
            if (nodes[cur].right != null)
                nodes.Add(nodes[cur].right);
            cur++;
        }

        foreach(var node in nodes)
            yield return node.val;
    }

    public override string ToString()
    {
        var l = this.ToEnumerable();
        return $"[{string.Join(", ", l)}]"; 
    }
}

// @lc code=start
public class Solution {
    public TreeNode SearchBST(TreeNode root, int val) {
        if (root == null || root.val == val) {
            return root;
        }
        else if(root.val > val) {
            return SearchBST(root.left, val);
        }
        else {
            return SearchBST(root.right, val);
        }
    }
}
// @lc code=end