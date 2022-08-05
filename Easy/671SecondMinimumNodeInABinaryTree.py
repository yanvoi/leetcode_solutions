# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        
        self.ans = float('inf')
        minimal = root.val
        
        def traverse(node):
            if node:
                if minimal < node.val < self.ans:
                    self.ans = node.val
                elif node.val == minimal:
                    traverse(node.left)
                    traverse(node.right)
                    
        traverse(root)
        return self.ans if self.ans < float('inf') else -1
        
