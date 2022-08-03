# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        if not head:
            return head
        
        dummy = ListNode(0)
        nodes = []
        
        while head:
            nodes.append(head)
            head = head.next
            
        nodes = nodes[:left-1] + nodes[left-1:right][::-1] + nodes[right:]
        dummy.next = nodes[0]
        
        for i in range(len(nodes)):
            nodes[i].next = nodes[i+1] if i+1 < len(nodes) else None
        
        return dummy.next
        
