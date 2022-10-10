class Solution:
    def findGCD(self, nums: List[int]) -> int:
        
        smallest = min(nums)
        biggest = max(nums)
        
        candidate = smallest
        
        while biggest % candidate != 0 or smallest % candidate != 0:
            candidate -= 1
            
        return candidate
        
