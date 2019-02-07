/**
 * Definition for singly-linked list. public class ListNode { int val; ListNode
 * next; ListNode(int x) { val = x; next = null; } }
 */
public class Solution {
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        ListNode A = headA;
        ListNode B = headB;
        if (A == null || B == null)
            return null;
        while (A != B) {
            if (A == null)
                A = headB;
            else
                A = A.next;
            if (B == null)
                B = headA;
            else
                B = B.next;
        }
        return A;
    }
}


// ListA + ListB = A + AB共有 + B + AB共有
// ListB + ListA = B + AB共有 + A + AB共有
