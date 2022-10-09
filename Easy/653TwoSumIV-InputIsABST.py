# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        
        self.exists = False
        self.needed = set()
        self.__traverse__(root, k)
        return self.exists
    
    def __traverse__(self, node, k):
        if self.exists or not node: return
        
        if node.val in self.needed:
            self.exists = True
            return
        
        self.needed.add(k - node.val)
        self.__traverse__(node.left, k)
        self.__traverse__(node.right, k)
        
