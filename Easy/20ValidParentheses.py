class Solution:
    def isValid(self, s: str) -> bool:
        
        available_chars = '(){}[]'
        opening = '({['
        
        stack = []
        
        for char in s:
            
            if char in available_chars:
                
                if char in opening:
                    stack.append(char)
                else:
                    if len(stack) == 0:
                        return False
                    
                    if char == ')' and stack[-1] == '(':
                        stack = stack[:-1]
                    elif char == '}' and stack[-1] == '{':
                        stack =stack[:-1]
                    elif char == ']' and stack[-1] == '[':
                        stack = stack[:-1]
                    else:
                        return False
                        
            else:
                return False
            
        if len(stack) != 0:
            return False
        
        return True
        
