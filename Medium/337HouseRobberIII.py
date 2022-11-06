# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        
        return max(self.__dfs__(root))
    
    
    def __dfs__(self, node):
        
        if not node:
            return [0, 0]
        
        L = self.__dfs__(node.left)
        R = self.__dfs__(node.right)
        # [we robbed children nodes, we did not rob children nodes]
        
        return [node.val + L[1] + R[1], max(L) + max(R)]
        
