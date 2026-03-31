class Solution:
    def isSame(self, x : Optional[TreeNode], y : Optional[TreeNode]):
            if not x and not y:
                return True
            if not x or not y :
                return False
            if x.val != y.val:
                return False
            return (self.isSame(x.left, y.left) and
            self.isSame(x.right, y.right))
    
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool: 
        # if not subRoot and not root:
        #     return True
        # elif subRoot or root:
        #     return False
        
        # res = False

        # def isSame(x : Optional[TreeNode], y : Optional[TreeNode]):
        #     if not x and not y:
        #         return True
        #     if not x or not y and x.val != y.val:
        #         return False
        #     return (isSame(x.left, y.left) and
        #     isSame(x.right, y.right))
        
        if not subRoot:
            return True
        if not root:
            return False
        if self.isSame(root, subRoot):
            return self.isSame(root,subRoot)
        
        return (self.isSubtree(root.left, subRoot) or
        self.isSubtree(root.right, subRoot))
        # return False
            
            