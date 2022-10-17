class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        
        ans = ''
        left = 0
        num_of_left = num_of_right = 0
        
        for i in range(len(s)):
            if s[i] == ')':
                num_of_right += 1
            elif s[i] == '(':
                num_of_left += 1
            
            if s[i] == ')' and num_of_left == num_of_right:
                ans += s[left+1:i]
                num_of_left = num_of_right = 0
                left = i+1
                
        return ans
        
