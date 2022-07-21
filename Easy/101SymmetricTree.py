# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        def traverse(node_one, node_two):
            
            if not node_one or not node_two:
                return node_one == node_two
            
            return node_one.val == node_two.val and traverse(node_one.left, node_two.right) and traverse(node_one.right, node_two.left)
 
        return not root or traverse(root.left, root.right)
