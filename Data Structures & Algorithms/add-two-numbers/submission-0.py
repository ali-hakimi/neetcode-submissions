# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = res = ListNode(0)
        cof = 0
        while l1 or l2 or cof:
            l1Val = l1.val if l1 else 0
            l2Val = l2.val if l2 else 0
            sum = l1Val + l2Val + cof
            cof = sum // 10
            rem = sum % 10
            res.next = ListNode(rem)
            res = res.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next