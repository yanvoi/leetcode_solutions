# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        def traverse(node):
            if node:
                if not node.left and not node.right:
                    yield node.val
                
                yield from traverse(node.left)
                yield from traverse(node.right)
        
        return list(traverse(root1)) == list(traverse(root2))
        
