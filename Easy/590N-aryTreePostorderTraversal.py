"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        
        def traverse(node, arr):
            if node:
                for child in node.children:
                    traverse(child, arr)
                arr.append(node.val)
                
        answer = []
        traverse(root, answer)
        
        return answer
        
