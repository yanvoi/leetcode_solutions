class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        
        ans, count = 0, 1
        
        for i in range(1, len(nums)):
            if nums[i] <= nums[i-1]:
                ans = max(ans, count)
                count = 0
                
            count += 1
                
        return max(ans, count)
    
