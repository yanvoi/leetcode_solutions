class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        
        digits = collections.Counter(str(n))
        
        return any(digits == collections.Counter(str(1 << b)) for b in range(31))
        
