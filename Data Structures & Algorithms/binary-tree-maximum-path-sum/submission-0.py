# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [root.val] # global variable

        def dfs(root : Optional[TreeNode] )->int:
            if not root:
                return 0
            
            left = max(dfs(root.left), 0)
            right = max(dfs(root.right), 0)

            # With split
            res[0] = max(res[0], left + right + root.val)

            # Without split
            return root.val + max(left, right)
        
        dfs(root)
        return res[0]
