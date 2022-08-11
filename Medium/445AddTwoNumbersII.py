# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        def to_string(node):
            string = ''
            while node:
                string = string + str(node.val)
                node = node.next
            return string
        
        num = str(int(to_string(l1)) + int(to_string(l2)))
        
        head = ListNode(int(num[0]))
        node = head
        
        for i in range(1, len(num)):
            node.next = ListNode(int(num[i]))
            node = node.next
            
        return head
        
