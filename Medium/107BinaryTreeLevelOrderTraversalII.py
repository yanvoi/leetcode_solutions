# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        def traverse(node, array, lvl):
            if node:
                if lvl == len(array):
                    array.append([])
                array[lvl].append(node.val)
                
                traverse(node.left, array, lvl+1)
                traverse(node.right, array, lvl+1)
        
        ans = []
        traverse(root, ans, 0)
        
        return ans[::-1]
        
