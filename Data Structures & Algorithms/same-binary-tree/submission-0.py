# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        elif not p or not q:
            return False
        l, r = self.isSameTree(p.left if p else None, q.left if q else None) , self.isSameTree(p.right if p else None , q.right if q else None)
        return p.val == q.val if l and r else False

        