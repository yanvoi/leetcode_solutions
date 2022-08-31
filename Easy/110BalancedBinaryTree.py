# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        self.Balanced = True
        self.__traverse__(root)
        return self.Balanced
    
    def __traverse__(self, node):
        
        if not node: return 0
        
        left, right = self.__traverse__(node.left), self.__traverse__(node.right)
        if abs(right - left) > 1: self.Balanced = False
            
        return max(left, right) + 1
        
