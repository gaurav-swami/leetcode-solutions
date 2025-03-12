
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        left = self.diameterOfBinaryTree(root.left)+1
        right = self.diameterOfBinaryTree(root.right)+1
        diameter = left+right
        return max(left,right)
