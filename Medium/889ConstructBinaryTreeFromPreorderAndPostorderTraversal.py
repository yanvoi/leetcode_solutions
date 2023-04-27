# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        
        self.preorder = preorder[::-1]
        self.postorder = postorder[::-1]
        return self._build()

    
    def _build(self):
        if not self.preorder:
            return None

        root = TreeNode(self.preorder.pop())
        if root.val != self.postorder[-1]:
            root.left = self._build()
        if root.val != self.postorder[-1]:
            root.right = self._build()

        if root.val == self.postorder[-1]:
            self.postorder.pop()
            
        return root
