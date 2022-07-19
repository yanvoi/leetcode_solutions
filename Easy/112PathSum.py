# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def traversal(node, sum, arr):
            if node:
                sum += node.val
                
                if not node.left and not node.right:
                    arr.append(sum)
                traversal(node.left, sum, arr)
                traversal(node.right, sum, arr)
        
        different_paths = []
        
        traversal(root, 0, different_paths)
        
        if targetSum in different_paths:
            return True
        return False
        
