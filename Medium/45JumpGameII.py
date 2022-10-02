class Solution:
    def jump(self, nums: List[int]) -> int:
        
        jumps, curEnd, curFarthest = 0, 0, 0
        
        for i in range(len(nums) - 1):
            curFarthest = max(curFarthest, i + nums[i])
            
            if curEnd == i:
                jumps += 1
                curEnd = curFarthest
                
        return jumps
        
