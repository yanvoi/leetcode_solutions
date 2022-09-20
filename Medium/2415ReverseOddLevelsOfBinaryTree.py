# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        q, nodes = collections.deque(), []
        if root: q.append(root)
            
        # bfs the tree and append next rows to array 'nodes'
        while q:
            size, row = len(q), []
            
            for _ in range(size):
                node = q.popleft()
                
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
                
                row.append(node)
                
            nodes.append(row)
            
        # for odd rows reverse the values
        for i in range(len(nodes)):
            if i % 2 == 0: continue
                
            left, right = 0, len(nodes[i]) - 1
            
            while left <= right:
                nodes[i][left].val, nodes[i][right].val = nodes[i][right].val, nodes[i][left].val
                left += 1
                right -= 1
        
        return root
        
