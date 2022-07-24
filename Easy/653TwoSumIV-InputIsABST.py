# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        
        def traverse(node, dic):
            if node:
                if node.val in dic:
                    dic[node.val] += 1
                else:
                    dic[node.val] = 1
                traverse(node.left, dic)
                traverse(node.right, dic)
        
        h = dict()
        traverse(root, h)
        
        for el in h:
            if el == k // 2:
                if h[el] > 1:
                    return True
            elif k - el in h.keys():
                return True

        return False
            
