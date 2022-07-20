class Solution:
    def addDigits(self, num: int) -> int:
        
        def add_digits(n):
            
            sum = 0
            
            while n > 0:
                
                sum += n % 10
                n = n // 10
                
            return sum
          
        # main part
            
        while num // 10 > 0:
            
            num = add_digits(num)
            
        return num
        
