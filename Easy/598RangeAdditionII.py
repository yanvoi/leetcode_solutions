class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        
        for operation in ops:
            m = min(m, operation[0])
            n = min(n, operation[1])
            
        return n*m
        
