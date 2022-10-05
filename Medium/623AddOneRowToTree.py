# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        
        # edge cases where input is invalid
        if not root or depth <= 0: return None
        
        # edge case where we have to insert the new node as the root of the tree
        if depth == 1: return TreeNode(val, root, None)
        
        # all other cases where we either insert the nodes or go further down the tree
        if depth == 2:
            root.left = TreeNode(val, root.left, None)
            root.right = TreeNode(val, None, root.right)
        else:
            self.addOneRow(root.left, val, depth - 1)
            self.addOneRow(root.right, val, depth - 1)
            
        return root
        
