# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #find middle, break
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        head2 =slow.next
        slow.next = None 
        #reverse
        prev = None
        curr = head2
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        p2 = prev
        #merge
        
        p1 = head
        while p2:
            next1 = p1.next
            next2 = p2.next
            p1.next = p2
            p2.next = next1
            p2 = next2
            p1 = next1
