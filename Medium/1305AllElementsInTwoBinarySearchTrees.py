# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        
        first, second, i, j, ans = [], [], 0, 0, []
        self.__traverse__(root1, first)
        self.__traverse__(root2, second)
        
        while i < len(first) or j < len(second):
            
            val1 = first[i] if i < len(first) else float('inf')
            val2 = second[j] if j < len(second) else float('inf')
            
            ans.append(min(val1, val2))
            if ans[-1] == val1:
                i += 1
            else:
                j += 1
        
        return ans
    
        
    def __traverse__(self, node, arr):
        if node:
            self.__traverse__(node.left, arr)
            arr.append(node.val)
            self.__traverse__(node.right, arr)
            
