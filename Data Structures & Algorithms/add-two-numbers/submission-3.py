# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = t = ListNode()
        c = 0
        while l1 and l2:
            ans = l1.val + l2.val + c
            c = ans//10
            if ans > 9 :
                ans = ans - 10
            t.next = ListNode(ans)
            t = t.next
            l1, l2 = l1.next, l2.next
        while c != 0:
            if l1:
                ans = c+l1.val
                l1 = l1.next
            elif l2:
                ans = c+l2.val
                l2 = l2.next
            else:
                ans = c
            c = 1 if ans == 10 else c//10
            if ans > 9 :
                ans = ans - 10
            t.next = ListNode(ans)
            t = t.next
        t.next = l1 if l1 else l2
        return dummy.next
