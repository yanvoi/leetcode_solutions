class Solution:
    def balancedStringSplit(self, s: str) -> int:
        
        L_count = R_count = 0
        ans = 0
        
        for char in s:
            if char == 'L':
                L_count += 1
            else:
                R_count += 1
                
            if L_count == R_count:
                ans += 1
                L_count = R_count = 0
                
        return ans
        
