/*
 * @lc app=leetcode id=206 lang=csharp
 *
 * [206] Reverse Linked List
 */

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public int val;
 *     public ListNode next;
 *     public ListNode(int val=0, ListNode next=null) {
 *         this.val = val;
 *         this.next = next;
 *     }
 * }
 */
// @lc code=start
public class Solution {
    public ListNode ReverseList(ListNode head) {
        if(head is null || head.next is null)
            return head;

        var rev = ReverseList(head.next);

        head.next.next = head;
        head.next = null;
        return rev;
    }
}
// @lc code=end

