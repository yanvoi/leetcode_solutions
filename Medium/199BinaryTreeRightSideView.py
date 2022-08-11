# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        stack, ans = collections.deque(), []
        if root: stack.append(root)
        
        while stack:
            cur_size = len(stack)
            
            for _ in range(cur_size):
                node = stack.popleft()
                if node.left: stack.append(node.left)
                if node.right: stack.append(node.right)
                
            ans.append(node.val)
            
        return ans
        
