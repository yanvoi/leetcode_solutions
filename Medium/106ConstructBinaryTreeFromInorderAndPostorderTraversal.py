# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        
        self.postorder = postorder
        self.index = dict()
        for i in range(len(inorder)):
            self.index[inorder[i]] = i
            
        return self.__build_tree__(0, len(inorder) - 1)
        
        
    def __build_tree__(self, start, end):
        
        if start > end: return None
        
        root = TreeNode(self.postorder.pop())
        root.right = self.__build_tree__(self.index[root.val] + 1, end)
        root.left = self.__build_tree__(start, self.index[root.val] - 1)
        
        return root
    
