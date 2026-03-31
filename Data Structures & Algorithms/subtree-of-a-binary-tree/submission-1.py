# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False
        if self.isSame(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def isSame(self, x:Optional[TreeNode], y:Optional[TreeNode]) -> bool:
        if not y and not x:
            return True
        if not y or not x or (y.val != x.val):
            return False
        return self.isSame(x.left, y.left) and self.isSame(x.right, y.right)
    