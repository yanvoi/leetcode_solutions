# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def has_one(node):
            
            if not node: return False
            
            left = has_one(node.left)
            if not left:
                node.left = None
                
            right = has_one(node.right)
            if not right:
                node.right = None
                
            return node.val == 1 or left or right
        
        return root if has_one(root) else None
        
