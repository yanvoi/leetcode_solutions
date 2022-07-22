# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        
        def traverse(node, arr, lower, higher):
            if node:
                if node.val < lower:
                    traverse(node.right, arr, lower, higher)
                elif node.val > higher:
                    traverse(node.left, arr, lower, higher)
                else:
                    arr.append(node.val)
                    traverse(node.left, arr, lower, higher)
                    traverse(node.right, arr, lower, higher)
        
        numbers = []
        traverse(root, numbers, low, high)
        sum = 0
        for num in numbers:
            sum += num
            
        return sum
        
