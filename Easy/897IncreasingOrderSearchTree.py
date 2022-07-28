# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        
        def traverse(node, arr):
            if node:
                traverse(node.left, arr)
                arr.append(node)
                traverse(node.right, arr)
                
        if not root:
            return []
        
        array = []
        traverse(root, array)
        
        root = node = array[0]
        for el in array[1:]:
            node.right = el
            node.left = None
            node = node.right
            
        node.right = node.left = None
        
        return root
        
