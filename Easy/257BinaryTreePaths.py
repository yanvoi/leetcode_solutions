 # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        
        def traverse(node):
            if not node:
                return []
              
            if not node.left and not node.right:
                return [str(node.val)]
                
            return [str(node.val)+'->'+ i for i in traverse(node.left)] + [str(node.val)+'->'+ i for i in traverse(node.right)]
        
        return traverse(root)
        
