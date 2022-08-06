# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        
        qo = []
        qo.append(original)
        
        qc = []
        qc.append(cloned)
        
        while qo:
            original_node = qo.pop()
            copied_node = qc.pop()
            
            if original_node == target:
                return copied_node
            
            if original_node.left:
                qo.append(original_node.left)
                qc.append(copied_node.left)
            
            if original_node.right:
                qo.append(original_node.right)
                qc.append(copied_node.right)
                
        return None
