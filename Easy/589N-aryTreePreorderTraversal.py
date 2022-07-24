"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        
        def traverse(node, arr):
            if node:
                arr.append(node.val)
                for child in node.children:
                    traverse(child, arr)
                
        answer = []
        traverse(root, answer)
        return answer
        
