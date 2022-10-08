class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        
        nums.sort()
        ans = float('inf')
        
        for left in range(len(nums) - 2):
            if left > 0 and nums[left-1] == nums[left]: continue
            
            mid, right = left + 1, len(nums) - 1
            
            while mid < right:
                cur = nums[left] + nums[mid] + nums[right]
                
                if cur == target: return target
                
                if abs(target - cur) < abs(target - ans):
                    ans = cur
                    
                if target > cur:
                    mid += 1
                else:
                    right -= 1
                    
        return ans
        
