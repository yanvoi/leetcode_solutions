# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        count, node = 0, head
        while node:
            count += 1
            node = node.next
            
        if count == 1: return None
        
        steps = (count // 2) - 1
        node = head
        
        for _ in range(steps):
            node = node.next
        node.next = node.next.next
        
        return head
        
