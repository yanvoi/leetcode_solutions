# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        
        self.postorder = postorder
        self.inorder_indexing = {num: index for index, num in enumerate(inorder)}
        return self._build_tree(0, len(postorder) - 1)

    
    def _build_tree(self, left_index, right_index):
        if left_index > right_index:
            return None

        root = TreeNode(self.postorder.pop())
        root.right = self._build_tree(self.inorder_indexing[root.val] + 1, right_index)
        root.left = self._build_tree(left_index, self.inorder_indexing[root.val] - 1)

        return root
    
