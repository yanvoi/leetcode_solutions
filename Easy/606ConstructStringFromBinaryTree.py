# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        def traverse(node):
            if node:
                if node.left and node.right:
                    return str(node.val) + "(" + str(traverse(node.left)) + ")" + "(" + str(traverse(node.right)) + ")"
                elif node.left and not node.right:
                    return str(node.val) + "(" + str(traverse(node.left)) + ")"
                elif not node.left and node.right:
                    return str(node.val) + "()" + "(" + str(traverse(node.right)) + ")"
                else:
                    return str(node.val)
            
        return traverse(root)
    
