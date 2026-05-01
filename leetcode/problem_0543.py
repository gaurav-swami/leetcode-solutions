# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def diameter(root:Optional[TreeNode])->List:
            if not root:
                return 0,0
            
            l_h,l_d = diameter(root.left)
            r_h,r_d = diameter(root.right)
            d = l_h+r_h
            return max(l_h,r_h)+1,max(l_d,r_d,d)
        return diameter(root)[1]
        