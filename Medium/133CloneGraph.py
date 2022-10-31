"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        
        if not node:
            return node
        
        q = collections.deque([node])
        
        # here we actually create the first copy node of the graph
        cloned = {node.val: Node(node.val)}
        
        while q:
            
            to_copy = q.popleft()
            cur_copy = cloned[to_copy.val]
            
            for neighb in to_copy.neighbors:
                # if we have not visited the node yet, we have to add it
                # to the queue and to the hashmap
                if neighb.val not in cloned:
                    cloned[neighb.val] = Node(neighb.val)
                    q.append(neighb)
                    
                # we add neighbors to the currently copied node's neighbors
                cur_copy.neighbors.append(cloned[neighb.val])
            
        
        return cloned[node.val]
        
