# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        
        stack, ans = collections.deque(), []
        
        if root: stack.append(root)
            
        while stack:
            size, maximum = len(stack), float('-inf')
            
            for _ in range(size):
                node = stack.popleft()
                if node.val > maximum:  maximum = node.val
                    
                if node.left: stack.append(node.left)
                if node.right: stack.append(node.right)
                    
            ans.append(maximum)
            
        return ans
        
