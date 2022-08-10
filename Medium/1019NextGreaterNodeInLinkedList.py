# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        
        stack = []
        answer = []
        index = 0
        
        while head:
            
            answer.append(0)
            val = head.val
            
            while stack and stack[-1][0] < val:
                last = stack.pop()
                answer[last[1]] = val
                
            stack.append((val, index))
            index += 1
            head = head.next
            
        return answer
    
