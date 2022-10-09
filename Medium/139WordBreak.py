class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        dp = [False] * len(s)
        
        for i in range(len(s)):
            for word in wordDict:
                cur = s[i-len(word)+1:i+1]
                
                if cur == word and (dp[i-len(word)] or i - len(word) < 0):
                    dp[i] = True
                    
        return dp[-1]
        
