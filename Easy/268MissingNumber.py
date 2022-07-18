class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        expected = (1 + len(nums)) * len(nums) // 2
        
        sum = 0
        
        for i in range(len(nums)):
            sum += nums[i]
            
        return expected - sum
        
