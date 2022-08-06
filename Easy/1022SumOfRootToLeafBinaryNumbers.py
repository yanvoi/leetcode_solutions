# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        
        def traverse(node):
            if not node:
                return []
            
            if not node.left and not node.right:
                return [str(node.val)]
            
            return [str(node.val) + i for i in traverse(node.left)] + [str(node.val) + i for i in traverse(node.right)]
        
        
        ans = 0
        paths = traverse(root)
        for num in paths:
            ans += int(num, 2)
            
        return ans
        
