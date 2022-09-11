# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        
        self.prevElement = TreeNode(float('-inf'))
        self.firstElement = None
        self.secondElement = None
        
        self.__find_swapped_elements__(root)
        
        self.firstElement.val, self.secondElement.val = self.secondElement.val, self.firstElement.val
    
    def __find_swapped_elements__(self, node):
        if not node: return
        
        self.__find_swapped_elements__(node.left)
        
        if not self.firstElement and self.prevElement.val >= node.val:
            self.firstElement = self.prevElement
            
        if self.firstElement and self.prevElement.val >= node.val:
            self.secondElement = node
            
        self.prevElement = node
        
        self.__find_swapped_elements__(node.right)
        
