class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        
        numbers = set(nums)
        
        while original in numbers:
            original *= 2
            
        return original
        
