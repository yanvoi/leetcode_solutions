# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def traverse(node, array):
            if node:
                traverse(node.left, array)
                array.append(node.val)
                traverse(node.right, array)
        
        arr = []
        traverse(root, arr)
        
        for i in range(len(arr) - 1):
            if arr[i] >= arr[i+1]:
                return False
            
        return True
        
