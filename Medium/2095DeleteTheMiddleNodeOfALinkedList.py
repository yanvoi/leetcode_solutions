# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head.next is None: return None
        
        # count the nodes in the list
        count, node = 0, head
        while node:
            count += 1
            node = node.next
        
        # count which node from the head to delete
        steps = (count // 2)
        
        # get the node that is a predecessor of the node to delete
        node = head
        for _ in range(steps - 1):
            node = node.next
            
        # delete it
        node.next = node.next.next
        
        return head
        
