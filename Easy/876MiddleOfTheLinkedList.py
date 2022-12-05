# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # here I have finally learned the slow and fast pointers technique
        slower_node = faster_node = head
        
        while faster_node and faster_node.next:
            faster_node = faster_node.next.next
            slower_node = slower_node.next
                
        return slower_node
        
