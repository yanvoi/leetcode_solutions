class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        
        n = str(bin(n))
        
        return all(n[i] != n[i+1] for i in range(len(n)-1))
        
