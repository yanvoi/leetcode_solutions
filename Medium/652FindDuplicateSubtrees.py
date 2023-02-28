# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        
        # just find all subtrees and hash (string --> root) their serialized forms
        self.subtree_serialized = defaultdict(list)
        self.dfs(root)
        # listed[0] because we can return any node that is a root of a repeated subtree
        return [listed[0] for subtree, listed in self.subtree_serialized.items() if len(listed) > 1]

    
    def dfs(self, root):
        if not root: return 'none'

        # preorder traversal
        current_subtree = str(root.val) + '|' + self.dfs(root.left) + '|' + self.dfs(root.right)
        self.subtree_serialized[current_subtree].append(root)

        return current_subtree
