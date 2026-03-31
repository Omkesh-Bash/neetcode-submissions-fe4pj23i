# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        q = deque()
        q.append(root)
        while q:
            qLen = len(q) # only for this level
            sub_lst = []
            for i in range(qLen):
                node = q.popleft()
                if node:
                    sub_lst.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if sub_lst: # only if there is a not null element
                res.append(sub_lst)
        return res