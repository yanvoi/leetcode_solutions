class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        s = s[::-1]
        
        count = 0
        i = 0
        
        while i < len(s) and s[i] == ' ':
            i += 1
        
        while i < len(s) and s[i] != ' ':
            count += 1
            i += 1
            
        return count
        
