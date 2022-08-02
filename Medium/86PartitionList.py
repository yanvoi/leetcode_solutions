# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        
        if not head:
            return head
        
        smaller = []
        bigger = []
        node = head
        
        while node:
            if node.val < x:
                smaller.append(node)
            else:
                bigger.append(node)
            node = node.next
            
        for i in range(len(smaller)):
            node = smaller[i]
            node.next = smaller[i+1] if i+1 < len(smaller) else None
            
        for i in range(len(bigger)):
            node = bigger[i]
            node.next = bigger[i+1] if i+1 < len(bigger) else None
            
        dummy = ListNode(0)
        
        if len(smaller) == 0:
            dummy.next = bigger[0]
        elif len(bigger) == 0:
            dummy.next = smaller[0]
        else:
            dummy.next = smaller[0]
            smaller[-1].next = bigger[0]
        
        return dummy.next
        
