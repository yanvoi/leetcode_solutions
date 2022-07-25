class Solution:
    def romanToInt(self, s: str) -> int:
        stack = list(s)
        answer = 0
        
        while stack:
            char = stack.pop()
            if char == 'I' and answer > 3:
                answer -= 1
            elif char == 'I':
                answer += 1
            elif char == 'V':
                answer += 5
            elif char == 'X' and answer >= 50:
                answer -= 10
            elif char == 'X':
                answer += 10
            elif char == 'L':
                answer += 50
            elif char == 'C' and answer >= 500:
                answer -= 100
            elif char == 'C':
                answer += 100
            elif char == 'D':
                answer += 500
            elif char == 'M':
                answer += 1000
                
        return answer
