class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        
        answer = 0
        
        for stone in stones:
            if stone in jewels:
                answer += 1
                
        return answer
    
