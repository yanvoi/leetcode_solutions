# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# O(n) time
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        bfs, even = collections.deque([root]), True
        while bfs:
            cur_size = len(bfs)
            level = []
            for _ in range(cur_size):
                node = bfs.popleft()
                level.append(node.val)
                if node.left: bfs.append(node.left)
                if node.right: bfs.append(node.right)

            if even and \
                (not all(num % 2 for num in level) \
                or not all(level[i] < level[i + 1] for i in range(len(level) - 1))): return False

            if not even and \
                (any(num % 2 for num in level) \
                or not all(level[i] > level[i + 1] for i in range(len(level) - 1))): return False

            even = not even

        return True
