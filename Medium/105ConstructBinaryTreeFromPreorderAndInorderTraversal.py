# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        def to_tree(left, right):
            nonlocal preorderIndex
            
            if left > right: return None
            
            root_value = preorder[preorderIndex]
            root = TreeNode(root_value)
            preorderIndex += 1
        
            root.left = to_tree(left, get_index[root_value]-1)
            root.right = to_tree(get_index[root_value]+1, right)
            
            return root
        
        
        get_index = dict()
        for index, num in enumerate(inorder):
            get_index[num] = index
            
        preorderIndex = 0
        
        return to_tree(0, len(preorder) - 1)
