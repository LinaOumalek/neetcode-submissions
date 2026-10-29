"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        copies = {}
        p1 = head
        dummy = Node(0)
        p2= dummy
        while p1:
            node = Node(p1.val)
            p2.next = node
            copies[p1] = node
            p1 = p1.next
            p2 = p2.next
        
        for node in copies:
            copy = copies[node]
            copy.random = copies.get(node.random)
        return dummy.next
