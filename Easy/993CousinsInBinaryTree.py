# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        
        def dfs(node, parent, depth, target):
            if node:
                if node.val == target:
                    return [parent, depth]
                
                return dfs(node.left, node, depth + 1, target) or dfs(node.right, node, depth + 1, target)
        
        left, right = dfs(root, None, 0, x), dfs(root, None, 0, y)
        return left[0] != right[0] and left[1] == right[1]
        
