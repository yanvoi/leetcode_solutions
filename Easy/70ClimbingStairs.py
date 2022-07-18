class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 2
        
        smaller = 1
        bigger = 2
        
        answer = 0
        
        for i in range(3, n + 1):
            answer = smaller + bigger
            
            smaller = bigger
            bigger = answer
            
        return answer
        
