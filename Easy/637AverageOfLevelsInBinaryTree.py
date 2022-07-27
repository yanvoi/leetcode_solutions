# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        
        def traverse(node, arr, lvl):
            if node:
                if not lvl < len(arr):
                    arr.append([])
                arr[lvl].append(node.val)
                
                traverse(node.left, arr, lvl+1)
                traverse(node.right, arr, lvl+1)
                
        array = [[]]
        traverse(root, array, 0)
        
        return [sum(level)/len(level) for level in array]
        
