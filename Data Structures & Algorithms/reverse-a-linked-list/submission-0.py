# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l = []
        t = head
        while t:
            l.append(t.val)
            t = t.next
        t = head
        for i in l[::-1]:
            t.val = i
            t = t.next
        return head