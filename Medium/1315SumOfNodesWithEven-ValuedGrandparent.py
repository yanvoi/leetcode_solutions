# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        
        self.answer = 0
        self.__traverse__(root, None, None)
        return self.answer
    
    def __traverse__(self, node, parent, grandparent):
        
        if not node: return
        
        if grandparent and grandparent.val % 2 == 0:
            self.answer += node.val

        self.__traverse__(node.left, node, parent)
        self.__traverse__(node.right, node, parent)
        
