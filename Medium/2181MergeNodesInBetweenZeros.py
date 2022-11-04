# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        prev = ListNode(0, head)
        node = head
        
        while node:
            if not node.next:
                prev.next = None
                return head
            
            to_merge = 0
            buf = node.next
            while buf and buf.val != 0:
                to_merge += buf.val
                buf = buf.next
            
            node.val = to_merge
            node.next = buf
            prev = node
            node = buf
            
        return None
        
