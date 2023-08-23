class Solution:
    def sumBase(self, n: int, k: int) -> int:
        return n % k + self.sumBase(n // k, k) if n else 0
        
