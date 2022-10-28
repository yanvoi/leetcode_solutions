# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        
        if n == 0: return []
        return self.__generate__(1, n+1)
    
    
    def __generate__(self, left, right):
        
        if left >= right:
            return None
        
        res = []
        for i in range(left, right):
            for l in self.__generate__(left, i) or [None]:
                for r in self.__generate__(i+1, right) or [None]:
                    node = ListNode(i)
                    node.left, node.right = l, r
                    res.append(node)
                    
        return res
        
