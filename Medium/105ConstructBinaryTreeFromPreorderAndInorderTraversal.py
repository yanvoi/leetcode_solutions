# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        self.preorder = preorder
        self.pre_index = 0
        
        self.index = dict()
        for i in range(len(inorder)):
            self.index[inorder[i]] = i
            
        return self.__build_tree__(0, len(inorder) - 1)
    
    
    def __build_tree__(self, start, end):
        
        if start > end: return None
        
        root = TreeNode(self.preorder[self.pre_index])
        self.pre_index += 1
        
        root.left = self.__build_tree__(start, self.index[root.val] - 1)
        root.right = self.__build_tree__(self.index[root.val] + 1, end)
        
        return root
        
