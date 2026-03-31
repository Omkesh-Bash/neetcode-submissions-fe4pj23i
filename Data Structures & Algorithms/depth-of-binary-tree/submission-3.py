# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        s = [[root, 1]]
        res = 0
        while s:
            n, d = s.pop()
            if n:
                res = max(d, res)
                s.append([n.left, d+1])
                s.append([n.right, d+1])
        return res