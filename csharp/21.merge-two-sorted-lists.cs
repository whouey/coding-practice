/*
 * @lc app=leetcode id=21 lang=csharp
 *
 * [21] Merge Two Sorted Lists
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
    public ListNode MergeTwoLists(ListNode list1, ListNode list2) {
        if (list1 == null && list2 == null)
            return null;
        else if (list1 == null || (list2 != null && list1.val > list2.val)) {
            list2.next = MergeTwoLists(list1, list2.next);
            return list2;
        }
        else {
            list1.next = MergeTwoLists(list1.next, list2);
            return list1;
        }
    }
}
// @lc code=end

