# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def are_the_same(first, second):
            
            if not first and not second:
                return True
            
            if not first or not second:
                return False
            
            return first.val == second.val and are_the_same(first.left, second.left) and are_the_same(first.right, second.right)
        
        
        def traverse(node, array):
            if node:
                traverse(node.left, array)
                array.append(node)
                traverse(node.right, array)
                
        arr = []
        traverse(root, arr)
        
        for node in arr:
            if are_the_same(node, subRoot):
                return True
            
        return False
