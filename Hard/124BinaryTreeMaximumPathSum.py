# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node):
            
            if not node: return 0
            
            left_gain = max(0, dfs(node.left))
            right_gain = max(0, dfs(node.right))
            
            cur_sum = node.val + left_gain + right_gain
            self.ans = max(self.ans, cur_sum)
            
            return node.val + max(left_gain, right_gain)
        
        self.ans = float('-inf')
        dfs(root)
        return self.ans
        
