# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        
        def is_uni(node, value):
            if node:
                return node.val == value and is_uni(node.left, value) and is_uni(node.right, value)
            return True
        
        if root:
            return is_uni(root, root.val)
        return False
        
