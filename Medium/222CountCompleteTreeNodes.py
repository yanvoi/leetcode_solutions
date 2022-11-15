# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        
        h = self.__height__(root)
        
        if h < 0:
            return 0
        
        if h == self.__height__(root.right) + 1:
            return (1 << h) + self.countNodes(root.right)
        
        return (1 << h-1) + self.countNodes(root.left)
        
        
    def __height__(self, node):
        h = 0
        while node:
            h += 1
            node = node.left
            
        return h - 1
        
