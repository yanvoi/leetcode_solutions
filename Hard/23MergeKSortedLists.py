# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        nodes = []
        for li in lists:
            node = li
            while node:
                nodes.append(node)
                node = node.next
                
        if len(nodes) == 0:
            return
                
        nodes.sort(key=lambda x: x.val)
        for i in range(len(nodes)-1):
            nodes[i].next = nodes[i+1]
            
        nodes[-1].next = None
        return nodes[0]
        
