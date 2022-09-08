# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        def traverse(node):
            if node:
                yield from traverse(node.left)
                yield node.val
                yield from traverse(node.right)
                
        return list(traverse(root))
        
