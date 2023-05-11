# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:

        def dfs(node):
            if not node: return 0, None

            left_depth, deepest_left = dfs(node.left)
            right_depth, deepest_right = dfs(node.right)

            if left_depth == right_depth: return left_depth + 1, node
            if left_depth > right_depth: return left_depth + 1, deepest_left
            return right_depth + 1, deepest_right

        return dfs(root)[1]
