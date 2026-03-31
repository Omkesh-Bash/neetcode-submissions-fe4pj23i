# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        f = head
        while f:
            f = f.next
            if f == head:
                return True
            f = f and f.next
            if f == head:
                return True
            head = head.next
        return False