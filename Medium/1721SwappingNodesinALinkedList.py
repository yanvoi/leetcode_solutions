# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        if not head: return head
        
        nodes = []
        while head:
            nodes.append(head)
            head = head.next
            
        nodes[k-1], nodes[-k] = nodes[-k], nodes[k-1]
        for i in range(len(nodes)):
            nodes[i].next = nodes[i+1] if i+1 < len(nodes) else None
            
        return nodes[0]
        
