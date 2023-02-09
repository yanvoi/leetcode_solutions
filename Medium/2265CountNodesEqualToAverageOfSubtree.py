# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        
        self.answer = 0
        self.dfs(root)
        return self.answer


    def dfs(self, root):

        if not root:
            return 0, 0

        left, right = self.dfs(root.left), self.dfs(root.right)

        if root.val == (root.val + left[0] + right[0]) // (1 + left[1] + right[1]):
            self.answer += 1

        return root.val + left[0] + right[0], 1 + left[1] + right[1]
