class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        
        answer = 0
        
        while x or y:
            first = x & 1
            second = y & 1
            
            if first != second:
                answer += 1
                
            x = x>>1
            y = y>>1
            
        return answer
        
