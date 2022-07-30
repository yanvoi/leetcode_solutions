class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        return sorted([el*el for el in nums])
        
