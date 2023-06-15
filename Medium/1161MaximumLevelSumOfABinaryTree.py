# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:

        max_sum, answer, cur_level = float('-inf'), -1, 0
        q = collections.deque([root])

        while q:
            size = len(q)
            cur_level_sum = 0
            cur_level += 1
            for _ in range(size):
                node = q.popleft()
                cur_level_sum += node.val
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)

            if cur_level_sum > max_sum:
                max_sum = cur_level_sum
                answer = cur_level

        return answer
