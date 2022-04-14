/*
 * @lc app=leetcode id=24 lang=csharp
 *
 * [24] Swap Nodes in Pairs
 */
 
using System.Collections;

var l = ListNode.FromEnumerable(new[] { 1, 2, 3, 4, 5, 6, 7 });
Console.WriteLine( new Solution().SwapPairs(l).ToString() );

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
    public ListNode SwapPairs(ListNode head) {
        if(head == null || head.next == null)
            return head;
        
        var temp = head.next;
        head.next = SwapPairs(head?.next?.next);
        temp.next = head;

        return temp;
    }
}
// @lc code=end

