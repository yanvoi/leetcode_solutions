# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# O(n) time, O(n) space
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        children = set(child for _, child, _ in descriptions)
        root_val = None
        self.info = defaultdict(list)
        for parent, child, is_left in descriptions:
            self.info[parent].append([child, is_left])
            if parent not in children: root_val = parent

        return self._buildBinaryTree(root_val)

    def _buildBinaryTree(self, node_val):
        node = TreeNode(node_val)
        if node_val not in self.info:
            return node

        left_val, right_val = None, None
        for child, is_left in self.info[node_val]:
            if is_left: left_val = child
            if not is_left: right_val = child

        node.left = self._buildBinaryTree(left_val) if left_val else None
        node.right = self._buildBinaryTree(right_val) if right_val else None

        return node
