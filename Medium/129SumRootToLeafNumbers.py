# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        self.answer = 0
        self.__SumRootToLeaf__(root, '')
        return self.answer
        
    def __SumRootToLeaf__(self, node, path):
            if node:
                path = path + str(node.val)
                if not node.left and not node.right:
                    self.answer += int(path)
                
                self.__SumRootToLeaf__(node.left, path)
                self.__SumRootToLeaf__(node.right, path)
                
