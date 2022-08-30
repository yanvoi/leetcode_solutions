# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        
        def tilt_sum(node, arr):
            if not node: return 0
            
            left = tilt_sum(node.left, arr)
            right = tilt_sum(node.right, arr)
            
            arr.append(abs(right - left))
            
            return right + left + node.val
                
        ans = []
        tilt_sum(root, ans)
        return sum(ans)
        
