class Solution:
    def minMaxGame(self, nums: List[int]) -> int:
        
        while len(nums) > 1:
            n = len(nums) // 2
            
            for i in range(n):
                if i % 2 == 0:
                    nums[i] = min(nums[2 * i], nums[2 * i + 1])
                else:
                    nums[i] = max(nums[2 * i], nums[2 * i + 1])
                    
            nums = nums[:n]
            
        return nums[0]
        
