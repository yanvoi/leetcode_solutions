class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        
        if n == 0:
            return False
        
        i = n
        
        while i > 1:
            i = i / 3
            
        if i == 1:
            return True
        
        return False
        
