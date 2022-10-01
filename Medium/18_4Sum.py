class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        nums.sort()
        ans = []
        
        for left in range(0, len(nums) - 3):
            
            if left > 0 and nums[left] == nums[left-1]: continue
            
            possible = self.__threeSum__(nums[left+1:], target - nums[left])
            
            for combination in possible:
                ans.append([nums[left]] + combination)
                
        return ans
        
        
    def __threeSum__(self, nums, target):
        
        ans = []
        
        for left in range(len(nums) - 2):
            
            if left > 0 and nums[left] == nums[left-1]: continue
            
            mid, right = left + 1, len(nums) - 1
            
            while mid < right:
                
                cur_sum = nums[left] + nums[mid] + nums[right]
                
                if cur_sum == target:
                    ans.append([nums[left]] + [nums[mid]] + [nums[right]])
                    
                    while mid < right and nums[mid] == nums[mid+1]:
                        mid += 1
                    while mid < right and nums[right] == nums[right-1]:
                        right -= 1
                        
                    mid += 1
                    right -= 1
                    
                elif cur_sum < target:
                    mid += 1
                else:
                    right -= 1
        
        return ans
        
