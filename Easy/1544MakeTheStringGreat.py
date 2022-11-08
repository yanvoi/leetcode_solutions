class Solution:
    def makeGood(self, s: str) -> str:
        
        stack = []
        
        for i, char in enumerate(s):
            if stack and char.isupper() and stack[-1] == char.lower():
                stack.pop()
            elif stack and char.islower() and stack[-1] == char.upper():
                stack.pop()
            else:
                stack.append(char)
                
        return ''.join(stack)
        
