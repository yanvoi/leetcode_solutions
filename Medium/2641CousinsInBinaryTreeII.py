# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        root.val = 0
        q = collections.deque([root])
        while q:
            next_sum = 0
            cur_level = []
            cur_size = len(q)
            for _ in range(cur_size):
                node = q.popleft()
                cur_level.append(node)
                if node.left:
                    next_sum += node.left.val
                    q.append(node.left)
                if node.right:
                    next_sum += node.right.val
                    q.append(node.right)

            for node in cur_level:
                left_val = node.left.val if node.left else 0
                right_val = node.right.val if node.right else 0
                if node.left: node.left.val = next_sum - left_val - right_val
                if node.right: node.right.val = next_sum - left_val - right_val
        
        return root
