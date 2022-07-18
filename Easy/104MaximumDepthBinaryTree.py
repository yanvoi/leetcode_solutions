# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        def tree_depth(node, depth):
            if not node:
                return depth
            return max(tree_depth(node.left, depth + 1), tree_depth(node.right, depth + 1))
        
        return tree_depth(root, 0)
        
