# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        if not root: return
        
        stack, ans = collections.deque(), 0
        stack.append(root)
        
        while stack:
            size = len(stack)
            
            for _ in range(size):
                node = stack.popleft()
                if node.right: stack.append(node.right)
                if node.left: stack.append(node.left)
                    
            ans = node.val
            
        return ans
        
