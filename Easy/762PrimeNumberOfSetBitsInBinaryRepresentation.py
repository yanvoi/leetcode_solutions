class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        
        @cache
        def is_prime(n):
            
            if n == 1: return False
            
            for i in range(2, n):
                if n % i == 0:
                    return False
                
            return True
        
        ans = 0
        for num in range(left, right+1):
            if is_prime(bin(num).count('1')):
                ans += 1
                
        return ans
        
