# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:

        self.to_delete = set(to_delete)
        self.answer = []
        self._dfs(root, True)
        return self.answer

    
    def _dfs(self, root, going_to_be_root):
        if not root:
            return root

        # case when we have to delete a node
        if root.val in self.to_delete:
            self._dfs(root.left, True)
            self._dfs(root.right, True)
            return None

        # case when we don't have to delete a node
        if going_to_be_root: self.answer.append(root)
        root.left = self._dfs(root.left, False)
        root.right = self._dfs(root.right, False)
        return root
        
