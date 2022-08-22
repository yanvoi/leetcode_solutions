class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        ans = []
        
        for left in range(len(nums) - 2):
            
            if left > 0 and nums[left] == nums[left-1]: continue

            mid, right = left + 1, len(nums) - 1
            while mid < right:
                cur_sum = nums[left] + nums[mid] + nums[right]
                
                if cur_sum < 0: mid += 1
                elif cur_sum > 0: right -= 1
                else:
                    ans.append([nums[left], nums[mid], nums[right]])
                    
                    while mid < right and nums[mid] == nums[mid+1]: mid += 1
                    while mid < right and nums[right] == nums[right-1]: right -= 1
                        
                    mid += 1
                    right -= 1
                    
        return ans
        
