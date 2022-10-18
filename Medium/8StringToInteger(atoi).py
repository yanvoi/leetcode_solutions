class Solution:
    def myAtoi(self, s: str) -> int:
        
        if not s: return 0
        
        max_int = 2 ** 31 - 1
        i, sign, ans = 0, 1, 0
        
        # ignoring white spaces
        while s[i] == ' ':
            i += 1
            if i == len(s): return 0
            
        # determining the sign if given
        if s[i] == '-' or s[i] == '+':
            if s[i] == '-':
                sign = -1
            i += 1
            
        # looping through the input and adding next digits to the answer
        # we need to keep in mind to not go out of bounds with our answer
        while i < len(s) and '0' <= s[i] <= '9':
            if ans > max_int // 10 or (ans == (max_int + 1) // 10 and ord(s[i]) - ord('0') > 7):
                if sign == 1:
                    return max_int
                
                return -1 * (max_int + 1)
            
            ans = ans * 10 + (ord(s[i]) - ord('0'))
            i += 1
        
        return sign * ans
        
