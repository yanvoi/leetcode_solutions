# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def contains_one(node):
            
            if not node: return False
            
            left = contains_one(node.left)
            right = contains_one(node.right)
            
            if not left: node.left = None
            if not right: node.right = None
                
            return node.val == 1 or left or right
        
        return root if contains_one(root) else None
        
