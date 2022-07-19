# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        def traversal(node, answer_list):
            if node.left:
                traversal(node.left, answer_list)
                
            answer_list.append(node.val)
            
            if node.right:
                traversal(node.right, answer_list)
        
        if not root:
            return []
                
        answer = []
        traversal(root, answer)
        
        return answer
        
