# O(n) time, O(1) space
class Solution:
    def maxDepth(self, s: str) -> int:
        answer, count = 0, 0
        for char in s:
            if char == '(': count += 1
            elif char == ')': count -= 1
            
            answer = max(answer, count)

        return answer
