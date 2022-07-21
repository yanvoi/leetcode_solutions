class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        
        if num == 1:
            return False
        
        root = int(math.sqrt(num))
        sum_of_divisors = 0
        
        for i in range(2, root + 1):
            if num % i == 0:
                sum_of_divisors += i + (num//i)
                
        return num == sum_of_divisors + 1
        
