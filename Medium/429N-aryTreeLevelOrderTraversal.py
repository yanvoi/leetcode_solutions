"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        
        stack, ans = collections.deque(), []
        if root: stack.append(root)
            
        while stack:
            size = len(stack)
            row = []
            
            for _ in range(size):
                node = stack.popleft()
                
                for x in node.children:
                    stack.append(x)
                    
                row.append(node.val)
                
            ans.append(row)
            
        return ans
        
