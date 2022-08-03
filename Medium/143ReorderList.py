# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return
        
        nodes = []
        while head:
            nodes.append(head)
            head = head.next
        
        left, right = 0, len(nodes) - 1
        ans = []
        while left < right:
            ans.append(nodes[left])
            ans.append(nodes[right])
            left, right = left+1, right-1
        if left == right:
            ans.append(nodes[left])
            
        for i in range(len(ans)):
            ans[i].next = ans[i+1] if i+1 < len(ans) else None
            
        head = ans[0]
        
