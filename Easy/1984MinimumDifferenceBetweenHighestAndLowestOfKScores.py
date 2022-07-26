class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        ans = 10000000
        
        for i in range(k-1, len(nums)):
            if nums[i] - nums[i-k+1] < ans:
                ans = nums[i] - nums[i-k+1]
                
        return ans
    
