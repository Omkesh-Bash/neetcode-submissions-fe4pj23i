# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = t = ListNode()
        c = 0
        while l1 or l2 or c!=0:
            i1 = l1.val if l1 else 0
            i2 = l2.val if l2 else 0
            ans = i1 + i2 + c
            c = ans // 10
            if ans > 9 :
                ans -=10
            t.next = ListNode(ans)
            t = t.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummy.next
        