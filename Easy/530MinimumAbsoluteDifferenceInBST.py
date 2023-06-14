# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if node:
                yield from dfs(node.left)
                yield node.val
                yield from dfs(node.right)

        first, second = dfs(root), dfs(root)
        next(second)
        return min(b - a for a, b in zip(first, second))
