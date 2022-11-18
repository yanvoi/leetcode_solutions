class Solution:
    def isUgly(self, n: int) -> bool:
        
        while n > 0 and (n % 2 == 0 or n % 3 == 0 or n % 5 == 0):
            if n % 2 == 0:
                n //= 2
            if n % 3 == 0:
                n //= 3
            if n % 5 == 0:
                n //= 5
                
        return n == 1
