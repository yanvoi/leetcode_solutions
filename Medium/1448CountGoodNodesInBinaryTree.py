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
        
    def __countGoodNodes__(self, node, greatest_so_far):
            if not node: return
            
            if node.val >= greatest_so_far:
                self.answer += 1
                
            # to every node we pass the greatest value among it's predecessors
            self.__countGoodNodes__(node.left, max(greatest_so_far, node.val))
            self.__countGoodNodes__(node.right, max(greatest_so_far, node.val))
    
