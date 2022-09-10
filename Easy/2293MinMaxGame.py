class Solution:
    def minMaxGame(self, nums: List[int]) -> int:
        
        divide = 1
        
        while len(nums) // divide > 1:
            divide = divide * 2
            n = len(nums) // divide
            
            for i in range(n):
                if i % 2 == 0:
                    nums[i] = min(nums[2 * i], nums[2 * i + 1])
                else:
                    nums[i] = max(nums[2 * i], nums[2 * i + 1])
            
        return nums[0]
        
