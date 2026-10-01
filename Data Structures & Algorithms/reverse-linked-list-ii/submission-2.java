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
    public ListNode reverseBetween(ListNode head, int left, int right) {
        ListNode dummy = new ListNode(0, head);
        ListNode leftPrev = dummy;
        ListNode cur = head;

        for (int i = 0; i < left - 1; i++) {
            leftPrev = cur;
            cur = cur.next;
        }

        ListNode prev = null;
        for (int i = left; i < right + 1 && cur != null; i++) {
            ListNode temp = cur.next;
            cur.next= prev;
            prev = cur;
            cur = temp;
        }

        leftPrev.next.next = cur;
        leftPrev.next = prev;
        return dummy.next;
    }
}