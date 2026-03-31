# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        s,f = head, head.next
        while f:
            if not f.next:
                break
            s = s.next
            f = f.next.next if f.next and f.next.next else None
        pre = None
        while s:
            n = s.next
            s.next = pre
            pre = s
            s = n
        while head :
            t = head.next
            head.next = pre
            pre = pre.next
            head.next.next = t
            head = t
