# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:

        self.total = self.__sum__(root)
        self.ans = 0
        self.__find_maximum__(root)
        return self.ans % (10**9 + 7)

    
    def __sum__(self, node):
        return node.val + self.__sum__(node.left) + self.__sum__(node.right) if node else 0

    def __find_maximum__(self, node):
        if not node: return 0

        left, right = self.__find_maximum__(node.left), self.__find_maximum__(node.right)
        self.ans = max(self.ans, (self.total - left) * left, (self.total - right) * right)

        return node.val + left + right
