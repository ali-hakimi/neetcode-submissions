/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */

class Solution {
    public ListNode mergeKLists(ListNode[] lists) {
        if (lists.length == 0) {
            return null;
        }
        if (lists.length == 1) {
            return lists[0];
        }

        int n = lists.length;
        int mid = n / 2;
        ListNode[] firstHalfList = Arrays.copyOfRange(lists, 0, mid);
        ListNode[] secondHalfList = Arrays.copyOfRange(lists, mid, n);
        ListNode firstHalfNode = mergeKLists(firstHalfList);
        ListNode secondHalfNode = mergeKLists(secondHalfList);

        return merge(firstHalfNode, secondHalfNode);
    }

    public ListNode merge(ListNode n1, ListNode n2) {
        if (n1 == null && n2 == null) {
            return null;
        }
        if (n1 == null) {
            return n2;
        }
        if (n2 == null) {
            return n1;
        }
        ListNode dummy = new ListNode(1);
        ListNode cur = dummy;

        while (n1 != null && n2 != null) {
            if (n1.val < n2.val) {
                cur.next = n1;
                n1 = n1.next;
            } else {
                cur.next = n2;
                n2 = n2.next;
            }
            cur = cur.next;
        }
        if (n1 != null) {
            cur.next = n1;
        }
        if (n2 != null) {
            cur.next = n2;
        }
        return dummy.next;
    }
}
