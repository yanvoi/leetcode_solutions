class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        ans = ''
        for i in range(len(s)):
            cur = self.get_longest(s, i, i)
            if len(cur) > len(ans): ans = cur
                
            cur = self.get_longest(s, i, i + 1)
            if len(cur) > len(ans): ans = cur
                
        return ans
    
    
    def get_longest(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left, right = left - 1, right + 1
        
        return s[left + 1:right]
        
