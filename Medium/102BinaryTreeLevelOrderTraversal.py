# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        queue = collections.deque()
        if root: queue.append(root)
        ret = []
            
        while queue:
            
            size, row = len(queue), []
            for _ in range(size):
                node = queue.popleft()
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
                    
                row.append(node.val)
                
            ret.append(row)
            
        return ret
        
