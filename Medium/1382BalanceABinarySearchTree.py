# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        
        arr = []
        self.__traverse__(root, arr)
        return self.__make_BST__(arr)
    
    def __traverse__(self, node, arr):
        if node:
            self.__traverse__(node.left, arr)
            arr.append(node.val)
            self.__traverse__(node.right, arr)
            
    def __make_BST__(self, arr):
        
        if len(arr) == 0: return None
        
        mid = len(arr) // 2
        
        root = TreeNode(arr[mid])
        root.left = self.__make_BST__(arr[:mid])
        root.right = self.__make_BST__(arr[mid+1:])
        
        return root
        
