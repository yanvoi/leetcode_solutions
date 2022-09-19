# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        
        q = collections.deque()
        if root: q.append(root)
        ans = 0
            
        while q:
            s = len(q)
            ans = 0
            
            for _ in range(s):
                node = q.popleft()
                ans += node.val
                
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
                    
        return ans
        
