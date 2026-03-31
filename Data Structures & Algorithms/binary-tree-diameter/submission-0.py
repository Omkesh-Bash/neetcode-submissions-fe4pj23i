# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0

        def getHeight(root: Optional[TreeNode]) -> int:
            if not root:
                return 0
            left_height = getHeight(root.left)
            right_height = getHeight(root.right)
            self.res = max(self.res, left_height + right_height)
            return max(left_height, right_height) + 1 
        getHeight(root)
        return self.res