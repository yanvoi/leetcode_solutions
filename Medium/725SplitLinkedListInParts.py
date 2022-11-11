# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        
        length = self.__get_length__(head)
        chunk_len, longer_chunks = length // k, length % k
        
        # subarray holds how many elements it should have
        ans = [chunk_len + 1] * longer_chunks + [chunk_len] * (k - longer_chunks)
        node, prev = head, None
        
        for i, num in enumerate(ans):
            if prev:
                prev.next = None
                
            ans[i] = node
            for _ in range(num):
                node, prev = node.next, node
                
        return ans
        
    
    def __get_length__(self, node):
        ret = 0
        while node:
            ret += 1
            node = node.next
            
        return ret
        
