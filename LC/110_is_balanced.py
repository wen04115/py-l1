# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
    #求子树高度
        def high(node):
            if node is None:
                return 0
            left_h= high(node.left)        
            right_h= high(node.right)
            return max(left_h,right_h)+1
        if root is None:
            return True
        left_high=high(root.left)
        right_high=high(root.right)
        if abs(left_high-right_high) >1:
          return False   
        return self.isBalanced(root.left) and self.isBalanced(root.right)