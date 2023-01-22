# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:

        self.answer = 0
        self.dfs(root)
        return self.answer


    def dfs(self, root):
        if not root: return 0

        # this formula is very tricky, has to do with the excess of all nodes
        left, right = self.dfs(root.left), self.dfs(root.right)
        self.answer += abs(left) + abs(right)

        return root.val + left + right - 1
