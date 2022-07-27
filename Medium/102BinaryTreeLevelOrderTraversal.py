# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root:
            return []
        
        def traversal(node, arr, lvl):
            if node:
                if not lvl < len(arr):
                    arr.append([])
                    
                arr[lvl].append(node.val)
                traversal(node.left, arr, lvl+1)
                traversal(node.right, arr, lvl+1)
        
        answer = [[]]
        traversal(root, answer, 0)
        
        return answer
