# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:

        # get the middle node of the list
        slow, fast = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # reverse the second part of the list
        cur, prev = slow, None
        while cur:
            cur.next, cur, prev = prev, cur.next, cur

        # iterate over twin nodes
        answer = 0
        while prev:
            answer = max(answer, prev.val + head.val)
            head = head.next
            prev = prev.next

        return answer
