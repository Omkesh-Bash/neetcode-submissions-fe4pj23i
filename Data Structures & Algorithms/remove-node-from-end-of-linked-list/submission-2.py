# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        l = d = ListNode(0, head)
        r = head
        while n > 0 and r:
            r = r.next
            n-=1
        while r:
            r = r.next
            l = l.next
        l.next = l.next.next
        return d.next