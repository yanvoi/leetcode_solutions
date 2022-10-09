class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums) < 3: return max(nums)
        
        for i in range(2, len(nums)):
            pre = nums[i-2] if i-2 >= 0 else 0
            prepre = nums[i-3] if i-3 >= 0 else 0
            
            nums[i] += max(pre, prepre)
            
        return max(nums[-1], nums[-2])
        
