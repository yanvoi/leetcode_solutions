class Solution:
    def isHappy(self, n: int) -> bool:
        
        def add_power_of_digits(number):
            sum = 0
            
            while number > 0:
                sum += pow((number % 10), 2)
                number = number // 10
                
            return sum
        
        numbers_used = set()
        
        while n != 1:
            
            if n in numbers_used:
                return False
            
            numbers_used.add(n)
            
            n = add_power_of_digits(n)
        
        return True
        
