# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head:
            return 
        
        def get_value(node):
            return node.val
        
        node = head
        
        arr = []
        while node:
            arr.append(node)
            node = node.next
            
        arr.sort(key=get_value)
        
        head = node = arr[0]
        for el in arr[1:]:
            node.next = el
            node = node.next
        node.next = None
        
        return head
        
