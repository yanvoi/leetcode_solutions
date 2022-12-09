# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:

        self.answer = 0
        self.__traverse__(root, None)
        return self.answer


    def __traverse__(self, node, parent):

        if not node:
            return parent.val, parent.val

        left = self.__traverse__(node.left, node)
        right = self.__traverse__(node.right, node)

        smallest = min(left[0], right[0])
        biggest = max(left[1], right[1])

        self.answer = max(self.answer, abs(node.val-biggest), abs(node.val-smallest))

        return min(smallest, node.val), max(biggest, node.val)
