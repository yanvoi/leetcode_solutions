class Solution:
    def isValid(self, s: str) -> bool:
        
        available_chars = set('(){}[]')
        opening = set('({[')
        
        stack = []
        
        for char in s:
            
            if char in available_chars:
                
                if char in opening:
                    stack.append(char)
                else:
                    if len(stack) == 0:
                        return False
                    
                    if char == ')' and stack[-1] == '(':
                        stack.pop()
                    elif char == '}' and stack[-1] == '{':
                        stack.pop()
                    elif char == ']' and stack[-1] == '[':
                        stack.pop()
                    else:
                        return False
                        
            else:
                return False
            
        if len(stack) != 0:
            return False
        
        return True
        
