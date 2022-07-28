class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                nums.insert(0, nums[i])
                nums.pop(i+1)
                
        return nums
        
