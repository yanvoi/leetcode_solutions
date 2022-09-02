# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        def traverse(node, path, all_possible, target):
            if node:
                path = path + [node.val]
                
                if not node.left and not node.right:
                    if sum(path) == target: all_possible.append(path)
                    return
                    
                traverse(node.left, path, all_possible, target)
                traverse(node.right, path, all_possible, target)
        
        paths = []
        traverse(root, [], paths, targetSum)
        return paths
        
