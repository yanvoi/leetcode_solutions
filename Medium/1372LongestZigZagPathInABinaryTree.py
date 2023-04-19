# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:

        def dfs(root):
            if not root:
                return -1, -1

            _, left = dfs(root.left)
            right, _ = dfs(root.right)

            self.answer = max(self.answer, left + 1, right + 1)
            return left + 1, right + 1


        self.answer = 0
        dfs(root)
        return self.answer
