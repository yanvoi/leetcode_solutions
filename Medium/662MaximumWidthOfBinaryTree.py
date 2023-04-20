# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        q = collections.deque()
        q.append((root, 1))
        answer = 0
        while q:
            q_size = len(q)
            answer = max(answer, q[-1][1] - q[0][1] + 1)
            for _ in range(q_size):
                node, num = q.popleft()
                if node.left:
                    q.append((node.left, num * 2))
                if node.right:
                    q.append((node.right, num * 2 + 1))

        return answer
