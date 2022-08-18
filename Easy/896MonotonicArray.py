class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        
        increasing = decreasing = True
        
        for i in range(1, len(nums)):
            
            if nums[i-1] < nums[i]:
                decreasing = False
            if nums[i-1] > nums[i]:
                increasing = False
                
        return increasing or decreasing
        
