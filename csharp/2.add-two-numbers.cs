/*
 * @lc app=leetcode id=2 lang=csharp
 *
 * [2] Add Two Numbers
 */
using System.Collections;


var l1 = ListNode.FromEnumerable(new[] { 2, 4, 3 });
var l2 = ListNode.FromEnumerable(new[] { 5, 6, 4 });
Console.WriteLine( new Solution().AddTwoNumbers(l1, l2).ToString() );


// Definition for singly-linked list.
public class ListNode {
    public int val;
    public ListNode next;
    public ListNode(int val=0, ListNode next=null) {
        this.val = val;
        this.next = next;
    }

    public static ListNode FromEnumerable(IEnumerable<int> enumerable) {
        var head = new ListNode();
        var cur = head;
        foreach(var item in enumerable){
            cur.next = new ListNode() { val = item };
            cur = cur.next;
        }
        return head.next;
    }

    public IEnumerable<int> ToEnumerable() {
        var cur = this;
        do {
            yield return cur.val;
            cur = cur.next;
        } while(cur != null); 
    }

    public override string ToString()
    {
        var l = this.ToEnumerable();
        return $"[{string.Join(", ", l)}]"; 
    }
}

// @lc code=start
public class Solution {
    public ListNode AddTwoNumbers(ListNode l1, ListNode l2) {
        var head = new ListNode();
        var cur = head;
        int carry = 0;

        while(l1 != null || l2 != null || carry != 0){
            int sum = (l1?.val??0) + (l2?.val??0) + carry;

            cur.next = new ListNode(){ val = sum%10 };
            cur = cur.next;

            carry = sum/10;
            l1 = l1?.next;
            l2 = l2?.next;
        }

        return head.next;
    }
}
// @lc code=end

