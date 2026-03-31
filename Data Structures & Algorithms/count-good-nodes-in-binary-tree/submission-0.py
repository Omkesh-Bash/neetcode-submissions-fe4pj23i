# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        return self.goodNodesHelper(root, root.val)

    def goodNodesHelper(self, node: TreeNode, max: int):
        if not node:
            return 0
        if node.val >= max:
            return self.goodNodesHelper(node.left, node.val) + self.goodNodesHelper(node.right, node.val) + 1
        return self.goodNodesHelper(node.left, max) + self.goodNodesHelper(node.right, max)