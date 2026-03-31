# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        l, t = 0, head
        while t:
            l+=1
            t = t.next
        t, i, h = 0, l-n-1, head
        if i == -1: return h.next
        while t < i:
            h = h.next
            t+=1
        h.next = h.next.next
        return head