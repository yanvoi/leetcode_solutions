class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        
        count = 0
        
        for i in range(len(s)):
            
            if s[i] == ' ':
                count += 1
                if count == k:
                    return s[:i]
        
        return s
        
