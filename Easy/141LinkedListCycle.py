# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        all_the_nodes = set()
        
        while head:
            if head in all_the_nodes:
                return True
            
            all_the_nodes.add(head)
            head = head.next
            
        return False
    
