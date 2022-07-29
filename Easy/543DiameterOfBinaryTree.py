# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        answer = [0]
        
        def get_path(node):
            
            if not node:
                return 0
            
            left = get_path(node.left)
            right = get_path(node.right)
            
            answer[0] = max(answer[0], left + right)
            
            return max(left, right) + 1
        
        get_path(root)
        return answer[0]
        
