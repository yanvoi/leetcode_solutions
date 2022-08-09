"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        def traverse(node, array):
            if node:
                array.append(node)
                traverse(node.child, array)
                traverse(node.next, array)
        
        if not head: return
        arr = []
        traverse(head, arr)
        
        for i in range(len(arr)):
            arr[i].child = None
            arr[i].prev = arr[i-1] if i-1 >= 0 else None
            arr[i].next = arr[i+1] if i+1 < len(arr) else None
            
        return arr[0]
        
