# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        
        def find_heads(tree_node, list_node, arr):
            if tree_node:
                find_heads(tree_node.left, list_node, arr)
                if tree_node.val == list_node.val:
                    arr.append(tree_node)
                find_heads(tree_node.right, list_node, arr)
                
                
        def list_in_tree(tree_node, head):
            
            if not head:
                return True
            
            if not tree_node and head:
                return False
            
            return tree_node.val == head.val and (list_in_tree(tree_node.left, head.next) or list_in_tree(tree_node.right, head.next))
        
        nodes = []
        find_heads(root, head, nodes)
        
        for node in nodes:
            
            if list_in_tree(node, head):
                return True
            
        return False
        
