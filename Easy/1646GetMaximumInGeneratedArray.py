class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        
        if n == 0:
            return 0
        
        nums = [0] * (n+1)
        nums[0] = 0
        nums[1] = 1
        
        for i in range(n):
            if 2 <= 2*i <= n:
                nums[2*i] = nums[i]
            if 2 <= 2*i+1 <= n:
                nums[2*i+1] = nums[i] + nums[i+1]
                
        return max(nums[:n+1])
