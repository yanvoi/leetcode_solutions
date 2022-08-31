# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        
        if not root: return 0
        
        left, right = self.minDepth(root.left), self.minDepth(root.right)
        
        if left == right == 0: return 1
        if left == 0 or right == 0:
            return max(left, right) + 1
        
        return min(left, right) + 1
        
