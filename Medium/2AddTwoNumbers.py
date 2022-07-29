# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        head = ListNode(0)
        node = head
        carry = 0
        
        while l1 != None or l2 != None or carry != 0:
            first = l1.val if l1 else 0
            second = l2.val if l2 else 0
            
            new_val = first + second + carry
            node.next = ListNode(new_val % 10)
            node = node.next
            carry = new_val // 10
            
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        return head.next
        
