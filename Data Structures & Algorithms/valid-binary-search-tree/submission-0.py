# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def bst(root : Optional[TreeNode], l, r):
            if not root:
                return True
            if l < root.val < r:
                left = bst(root.left, l, root.val)
                right = bst(root.right, root.val, r)
                return left and right
            return False
        
        return bst(root, float("-infinity"), float("infinity"))