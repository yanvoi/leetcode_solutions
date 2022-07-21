# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        answer = 0
        stack = [[root, 'right']]
            
        while stack:
            node, pos = stack.pop()
                
            if node:
                if pos == 'left' and not node.left and not node.right:
                    answer += node.val
                        
                stack.append([node.left, 'left'])
                stack.append([node.right, 'right'])

        return answer
