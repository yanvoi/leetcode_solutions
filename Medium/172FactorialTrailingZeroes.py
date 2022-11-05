class Solution:
    def trailingZeroes(self, n: int) -> int:
        
        # you have to know the math trick in order to get it
        # very boring question
        ans = 0
        divide = 5
        
        while divide <= n:
            ans += n // divide
            divide *= 5
            
        return ans
        
