# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        
        self.frequency = defaultdict(int)
        self.max_frequency = 0
        self.dfs(root)
        return [key for key, freq in self.frequency.items() if freq == self.max_frequency]


    def dfs(self, root):

        if not root: return 0

        subtree_sum = root.val + self.dfs(root.left) + self.dfs(root.right)
        self.frequency[subtree_sum] += 1
        self.max_frequency = max(self.max_frequency, self.frequency[subtree_sum])

        return subtree_sum
