# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        self.bigger_sum = 0
        self.__traverse__(root)
        return root
    
    
    def __traverse__(self, root):
        
        if not root:
            return
        
        self.__traverse__(root.right)
        root.val = self.bigger_sum = self.bigger_sum + root.val
        self.__traverse__(root.left)
        
