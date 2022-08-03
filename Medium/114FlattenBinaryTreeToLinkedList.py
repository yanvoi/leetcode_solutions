# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        
        def traverse(node, arr):
            if node:
                arr.append(node)
                traverse(node.left, arr)
                traverse(node.right, arr)
            else:
                return None
                
        nodes = []
        traverse(root, nodes)
        
        for i in range(len(nodes)):
            nodes[i].left = None
            nodes[i].right = nodes[i+1] if i+1 < len(nodes) else None
        
