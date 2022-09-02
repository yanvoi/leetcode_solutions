class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        
        nums.sort()
        ans = nums[0] + nums[1] + nums[2]
        
        for left in range(len(nums) - 2):
            mid, right = left + 1, len(nums) - 1
            
            while mid < right:
                cur_sum = nums[left] + nums[mid] + nums[right]
                
                if cur_sum == target:
                    return cur_sum
                
                if abs(cur_sum - target) < abs(ans - target):
                    ans = cur_sum
                    
                if cur_sum > target:
                    right -= 1
                else:
                    mid += 1
                    
        return ans
        
