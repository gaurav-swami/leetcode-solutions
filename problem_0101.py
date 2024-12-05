class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def isSubtreeSymmetric(root1: Optional[TreeNode], root2: Optional[TreeNode])->bool:
             
            if not root1 and not root2:
                return True
            if not root1 or not root2:
                return False
            
            return root1.val == root2.val and isSubtreeSymmetric(root1.left,root2.right) and isSubtreeSymmetric(root1.right,root2.left)

        return isSubtreeSymmetric(root.left,root.right)
            