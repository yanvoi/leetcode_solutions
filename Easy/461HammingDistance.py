class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        
        answer = 0
        
        while x or y:
            
            if x & 1 != y & 1:
                answer += 1
                
            x = x>>1
            y = y>>1
            
        return answer
        
