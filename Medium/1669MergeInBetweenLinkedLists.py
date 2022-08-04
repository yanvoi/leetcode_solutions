# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        head, i = list1, 0
        
        while i < a-1:
            head = head.next
            i += 1
        first = head
        
        while i < b:
            head = head.next
            i += 1
        second = head.next
        
        node = list2
        first.next = node
        
        while node.next:
            node = node.next
        node.next = second
        
        return list1
        
