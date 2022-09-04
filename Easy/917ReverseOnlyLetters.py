class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        
        left, right = 0, len(s) - 1
        ans = [''] * len(s)
        
        while left <= right:
            if not s[left].isalpha():
                ans[left] = s[left]
                left += 1
                continue
            if not s[right].isalpha():
                ans[right] = s[right]
                right -= 1
                continue
                
            ans[left], ans[right] = s[right], s[left]
            left += 1
            right -= 1
            
        return ''.join(ans)
        
