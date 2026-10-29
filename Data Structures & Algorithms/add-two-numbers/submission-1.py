# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        p3 = dummy
        c = 0
        while l1 or l2:
            if not l1:
                a = 0
            else:
                a = l1.val
            if not l2:
                b = 0
            else:
                b = l2.val
            total = a + b + c
            val = total % 10
            c = total // 10
            p3.next = ListNode(val)
            if l1:
                l1 = l1.next
            if l2:
                l2= l2.next
            p3 = p3.next

        if c:
            p3.next = ListNode(c)
        return dummy.next



