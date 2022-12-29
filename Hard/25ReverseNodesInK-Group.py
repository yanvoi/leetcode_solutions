# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        dummy = prev_k_nodes = ListNode()
        dummy.next = left = right = head

        while True:
            count = 0
            while right and count < k:
                right = right.next
                count += 1

            if count < k:
                return dummy.next

            cur, prev = left, right
            for _ in range(k):
                tmp = cur.next
                cur.next = prev
                prev = cur
                cur = tmp

            prev_k_nodes.next = prev
            prev_k_nodes = left
            left = right
