# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        # this function goes through the whole linked list appending values from it to another list
        def linked_to_normal(node, our_list):
            if node:
                our_list.append(node.val)
                linked_to_normal(node.next, our_list)
                
        list_to_check = []
        
        linked_to_normal(head, list_to_check)
        
        if list_to_check == list_to_check[::-1]:
            return True
    
        return False
        
