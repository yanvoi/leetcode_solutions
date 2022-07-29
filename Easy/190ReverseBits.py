class Solution:
    def reverseBits(self, n: int) -> int:
        
        answer = 0
        
        for i in range(32):
            
            bit = (n >> i) & 1
            answer = answer | (bit << (31-i))
            
        return answer
        
