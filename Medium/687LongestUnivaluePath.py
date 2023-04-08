# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        
        self.answer = 0
        self._dfs(root)
        return self.answer

    
    def _dfs(self, root):
        if not root: return 0

        left_streak = self._dfs(root.left)
        right_streak = self._dfs(root.right)

        left = left_streak + 1 if root.left and root.left.val == root.val else 0
        right = right_streak + 1 if root.right and root.right.val == root.val else 0

        self.answer = max(self.answer, left + right)
        return max(left, right)
