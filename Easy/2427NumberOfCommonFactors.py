class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        
        ans, divider = 0, 1
        
        while divider <= min(a, b):
            ans += (a % divider == 0) and (b % divider == 0)
            divider += 1
        
        return ans
        
