# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        
        self.answer, self.smaller = float('inf'), float('-inf')
        self.dfs(root)
        return self.answer


    def dfs(self, root):

        if root.left:
            self.dfs(root.left)

        self.answer = min(self.answer, root.val - self.smaller)
        self.smaller = root.val

        if root.right:
            self.dfs(root.right)
