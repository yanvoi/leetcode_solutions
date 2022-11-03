class Solution:
    def makeIntegerBeautiful(self, n: int, target: int) -> int:
        
        def sum_digits(num):
            ret = 0
            while num > 0:
                ret += num % 10
                num = num // 10
            
            return ret
        
        add = 0
        tens = 1
        # we try to make the number smaller from the right side
        # since that's gonna give us the smallest solution
        while sum_digits(n) > target:
            
            add += tens * (10 - (n % 10))
            tens *= 10
            n = (n // 10) + 1
            
        return add
        
