class Solution:
    def countEven(self, num: int) -> int:
        
        def has_even_digits(number):
            
            count = 0
            
            while number > 0:
                count += number % 10
                number = number // 10
            
            return count % 2 == 0
        
        return sum([1 for i in range(1, num+1) if has_even_digits(i)])
        
