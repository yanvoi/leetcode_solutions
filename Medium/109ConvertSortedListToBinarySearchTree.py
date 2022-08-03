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
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        
        # converting a sorted list to a BST
        def to_bst(array):
            
            if len(array) == 0:
                return None
            
            if len(array) == 1:
                return TreeNode(array[0])
            
            mid = len(array) // 2
            root = TreeNode(array[mid])
            
            root.left = to_bst(array[:mid])
            root.right = to_bst(array[mid+1:])
            
            return root
        
        # main part of the program
        arr = []
        while head:
            arr.append(head.val)
            head = head.next
        
        return to_bst(arr)
        
