# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:

        self.answer = 0
        self.count = [0] * 10
        self._dfs(root)
        return self.answer

    
    def _dfs(self, root):
        if not root: return

        self.count[root.val] += 1
        if root.left or root.right:
            self._dfs(root.left)
            self._dfs(root.right)
        else:
            self.answer += sum(digit % 2 != 0 for digit in self.count) <= 1

        self.count[root.val] -= 1
