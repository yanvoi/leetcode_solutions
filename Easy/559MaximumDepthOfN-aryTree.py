"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        
        if not root:
            return 0
        
        def traverse(node, depths, current):
            if node:
                current += 1
                if len(node.children) == 0:
                    depths.append(current)
                else:
                    for child in node.children:
                        traverse(child, depths, current)
                        
        dep = []
        traverse(root, dep, 0)
        
        return max(dep)
