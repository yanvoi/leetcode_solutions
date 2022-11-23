# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def bstToGst(self, root: TreeNode) -> TreeNode:
        
        self.bigger_sum = 0
        self.__traverse__(root)
        return root
        
    def __traverse__(self, root):
        
        if root:
            self.__traverse__(root.right)
            root.val = self.bigger_sum = self.bigger_sum + root.val
            self.__traverse__(root.left)
