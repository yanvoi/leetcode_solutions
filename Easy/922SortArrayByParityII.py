class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        
        for i in range(len(nums)):
            if i % 2 == 0 and nums[i] % 2 != 0:
                j = i + 1
                while nums[j] % 2 != 0:
                    j += 1
                nums[i], nums[j] = nums[j], nums[i]
                    
            elif i % 2 != 0 and nums[i] % 2 == 0:
                j = i + 1
                while nums[j] % 2 == 0:
                    j += 1
                nums[i], nums[j] = nums[j], nums[i]
                
        return nums
    
