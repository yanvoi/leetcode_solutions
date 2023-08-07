# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        while node and node.next:
            buff = node.next
            new_node = ListNode(gcd(node.val, buff.val), buff)
            node.next = new_node
            node = buff

        return head
