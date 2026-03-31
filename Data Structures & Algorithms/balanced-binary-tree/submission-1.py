# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.res = True
        def helper(root : Optional[TreeNode]):
            if not root:
                return 0
            left = helper(root.left)
            right = helper(root.right)
            if left - right not in [-1, 0, 1]:
                self.res = False
            return max(left, right) + 1
        helper(root)
        return self.res