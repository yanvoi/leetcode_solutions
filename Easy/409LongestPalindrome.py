class Solution:
    def longestPalindrome(self, s: str) -> int:
        
        h = dict()
        for char in s:
            if char in h:
                h[char] += 1
            else:
                h[char] = 1
                
        is_odd = False
        ans = 0
        
        for char in h:
            if h[char] % 2 != 0:
                is_odd = True
            ans += (h[char] // 2) * 2
            
        if is_odd:
            ans += 1
            
        return ans
        
