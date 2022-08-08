# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        
        def traverse(node, pre, cur):
            if not node: return

            traverse(node.left, pre, cur)
            
            cur[0] = min(cur[0], node.val - pre[0])
            pre[0] = node.val
            
            traverse(node.right, pre, cur)
                
                
        pre, cur = [float('-inf')], [float('inf')]
        traverse(root, pre, cur)
        
        return cur[0]
        
