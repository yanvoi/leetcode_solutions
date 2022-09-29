class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        left, right = 0, len(s) - 1
        
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
                continue
            
            first = s[:left] + s[left+1:]
            second = s[:right] + s[right+1:]
            return first == first[::-1] or second == second[::-1]
        
        return True
        
