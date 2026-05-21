# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        p1, p2 = head, head 
        l = 0
        while p1:
            l += 1
            p1 = p1.next
        target = l - n - 1
        if target == -1:
            return head.next
        for i in range(target):
            p2 = p2.next
        p2.next = p2.next.next
        return head
        
        

