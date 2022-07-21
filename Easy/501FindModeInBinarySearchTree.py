# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        
        def traverse(node, func_hash):
            if node:
                if node.val in func_hash:
                    func_hash[node.val] += 1
                else:
                    func_hash[node.val] = 1
                traverse(node.left, func_hash)
                traverse(node.right, func_hash)
        
        our_hash = dict()
        traverse(root, our_hash)
        
        count = max(our_hash.values())
        
        answer = []
        
        for element in our_hash:
            if our_hash[element] == count:
                answer.append(element)
                
        return answer
        
