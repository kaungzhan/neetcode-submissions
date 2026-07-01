# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        groupPrev = dummy
        while True:
            kth_node = self.getKthNode(groupPrev, k)
            if kth_node is None:
                break
            groupNext = kth_node.next
            prev, curr = groupNext, groupPrev.next
            while curr != groupNext:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            tmp = groupPrev.next
            groupPrev.next = prev
            groupPrev = tmp
        return dummy.next

    
    def getKthNode(self, groupPrev: Optional[ListNode], k: int) -> Optional[ListNode]:
        for _ in range(k):
            if groupPrev is None:
                return None
            groupPrev = groupPrev.next
        return groupPrev 
        