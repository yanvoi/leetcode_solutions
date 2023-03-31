# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# the problem is explained very poorly
# what we basically need to do is count the number of non-connected groups of numbers from nums
class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:

        answer = 0
        numbers = set(nums)

        while head:
            if head.val in numbers and (head.next is None or head.next.val not in numbers):
                answer += 1
            
            head = head.next

        return answer
