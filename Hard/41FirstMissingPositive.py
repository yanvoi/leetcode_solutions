class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # not done with constant extra space!!!
        missing = [True] * len(nums)
        
        for i in range(len(nums)):
            if 0 < nums[i] <= len(nums):
                missing[nums[i]-1] = False
                
        for i in range(len(missing)):
            if missing[i]:
                return i+1
            
        return len(nums)+1
        
