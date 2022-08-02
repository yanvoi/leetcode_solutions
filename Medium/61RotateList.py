# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        def rotate_list(arr, r):
            return arr[r:]+arr[:r]
        
        if not head:
            return head
        
        nodes = []
        while head:
            nodes.append(head)
            head = head.next
            
        nodes = rotate_list(nodes, -1*(k%len(nodes)))
        head = nodes[0]
        for i in range(len(nodes)):
            nodes[i].next = nodes[i+1] if i+1 < len(nodes) else None

        return head    
        
