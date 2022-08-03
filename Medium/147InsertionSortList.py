# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # sorting it in the array is way simpler
        # don't want to over complicate a simple task
        
        def to_array(node):
            array = []
            while node:
                array.append(node)
                node = node.next
            return array
        
        if not head:
            return head
        
        # turning the linked list into an array of nodes
        nodes = to_array(head)
        
        # sorting part
        # if you put:
        # nodes.sort(key=lambda x: x.val)
        # instead of the manual insert sort
        # it will be much faster
        # but the specification required the insert sort to be used
        for i in range(1, len(nodes)):
            dummy, j = nodes[i], i
            while j > 0 and dummy.val < nodes[j-1].val:
                nodes[j] = nodes[j-1]
                j -= 1
            nodes[j] = dummy
            
        # changing .next pointer for each node in the sorted array
        for i in range(len(nodes)):
            nodes[i].next = nodes[i+1] if i+1 < len(nodes) else None
            
        return nodes[0]
        
