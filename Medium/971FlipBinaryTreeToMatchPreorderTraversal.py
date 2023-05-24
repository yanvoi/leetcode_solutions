# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# simple DFS solution - simply traverse the tree checking if the values in voyage match
class Solution:
    def flipMatchVoyage(self, root: Optional[TreeNode], voyage: List[int]) -> List[int]:

        self.answer = []
        self.voyage = voyage
        self.cur_index = 0
        self._dfs(root)

        return self.answer if -1 not in self.answer else [-1]

    
    def _dfs(self, root):
        if not root:
            return

        if root.val != self.voyage[self.cur_index]:
            self.answer.append(-1)
            return

        self.cur_index += 1
        if root.left and root.left.val != self.voyage[self.cur_index]:
            self.answer.append(root.val)
            root.left, root.right = root.right, root.left

        self._dfs(root.left)
        self._dfs(root.right)
