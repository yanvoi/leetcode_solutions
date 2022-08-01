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
            
        if len(smaller) == 0:
            return head
                
        for i in range(len(smaller) -1):
            node = smaller[i]
            node.next = smaller[i+1]
            
        if len(bigger) == 0:
            return smaller[0]
        
        if len(smaller) < 2:
            node = smaller[0]
            node.next = bigger[0]
        else:
            node = node.next
            node.next = bigger[0]
        
        for i in range(len(bigger) - 1):
            node = bigger[i]
            node.next = bigger[i+1]
        node = node.next
        node.next = None
        return smaller[0]
        
