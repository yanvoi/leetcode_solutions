# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        def traverse(node, array):
            if node:
                traverse(node.left, array)
                array.append(node.val)
                traverse(node.right, array)
                
        l = []
        traverse(root, l)
        return l[k-1]
        
