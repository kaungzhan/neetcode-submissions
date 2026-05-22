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
        p1, p2 = head, head 
        new_ll = {}
        while p1:
            new_ll[p1] = Node(p1.val)
            p1 = p1.next
        while p2:
            new_ll[p2].next = new_ll.get(p2.next)
            new_ll[p2].random = new_ll.get(p2.random)
            p2 = p2.next
        return new_ll.get(head)