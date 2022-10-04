class Solution:
    def checkString(self, s: str) -> bool:
        
        b_appeared = False
        
        for char in s:
            if char == 'b':
                b_appeared = True
            elif char == 'a' and b_appeared:
                return False
            
        return True
        
