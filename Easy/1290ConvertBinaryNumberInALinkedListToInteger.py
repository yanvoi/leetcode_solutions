# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        digits = []
        while head:
            digits.insert(0, head.val)
            head = head.next
            
        ans = 0
        for i in range(len(digits)):
            if digits[i] == 1:
                ans += 2**i
                
        return ans
    
