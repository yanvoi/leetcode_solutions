# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
                
        self.answer = 0
        self.__countGoodNodes__(root, root.val)
        return self.answer
        
    def __countGoodNodes__(self, node, biggest_so_far):
            if not node: return
            
            if node.val >= biggest_so_far:
                self.answer += 1
                biggest_so_far = node.val
                
            self.__countGoodNodes__(node.left, biggest_so_far)
            self.__countGoodNodes__(node.right, biggest_so_far)
    
