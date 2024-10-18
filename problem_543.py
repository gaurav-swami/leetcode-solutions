class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def diameter(root):
            if not root:
                return 0,0
            
            left_height, left_diam = diameter(root.left)
            right_height, right_diam = diameter(root.right)
            curr_diam = left_height + right_height 

            return max(left_height,right_height)+1, max(left_diam,right_diam,curr_diam)
        
        return diameter(root)[1]