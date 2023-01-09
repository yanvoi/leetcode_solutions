# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        return [val for val in self.preorderGenerator(root)]


    def preorderGenerator(self, root):
        if root:
            yield root.val
            yield from self.preorderGenerator(root.left)
            yield from self.preorderGenerator(root.right)
