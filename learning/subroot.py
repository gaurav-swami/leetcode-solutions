class Solution:
    def isIdentical(self,root: Optional[TreeNode], subRoot: Optional[TreeNode])->bool:
        if not root and not subRoot:
            return True

        if not root or not subRoot:
            return False

        if root.val == subRoot.val:
            return self.isIdentical(root.left, subRoot.left) and self.isIdentical(root.right, subRoot.right)
        else:
            return False

    def isSubtree (self,root: Optional[TreeNode],subRoot: Optional[TreeNode] )->bool:
        if not subRoot:
            return True

        if not root :
            return False

        if root.val == subRoot.val:
            if self.isIdentical(root,subRoot):
                return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot) 