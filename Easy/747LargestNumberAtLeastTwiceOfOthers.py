class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        
        if len(nums) == 0:
            return -1
        
        biggest = 0
        
        for i in range(1, len(nums)):
            if nums[i] > nums[biggest]:
                biggest = i
                
        second_biggest = (biggest + 1) % len(nums)
                
        for i in range(len(nums)):
            if i != biggest and nums[i] > nums[second_biggest]:
                second_biggest = i   
            
        if nums[biggest] >= nums[second_biggest] * 2:
            return biggest
        else:
            return -1
        
