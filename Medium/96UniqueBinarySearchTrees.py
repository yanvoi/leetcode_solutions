class Solution:
    def numTrees(self, n: int) -> int:
        
        dp = [1] * (n + 1)
        
        for level in range(2, n+1):
            cur = 0
            for root in range(1, level+1):
                cur += dp[level - root] * dp[root - 1]
            dp[level] = cur
            
        return dp[n]
        
