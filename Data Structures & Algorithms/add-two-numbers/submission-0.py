# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        p1, p2, p3 = l1, l2, dummy
        sum_val = 0
        carry,stay = 0, 0
        while p1 or p2:
            if p1 and p2:
                sum_val = p1.val + p2.val + carry
                p1 = p1.next 
                p2 = p2.next
            elif p1:
                sum_val = p1.val + 0 + carry
                p1 = p1.next 
            else:
                sum_val = 0 + p2.val + carry
                p2 = p2.next
            carry = sum_val // 10
            stay = sum_val % 10
            p3.next = ListNode(stay)
            p3 = p3.next 
        if carry != 0 :
            p3.next = ListNode(carry)
        return dummy.next

