class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # not done with constant extra space!!!
        missing = [True] * len(nums)
        
        for i in range(len(nums)):
            if 0 < nums[i] <= len(nums):
                missing[nums[i]-1] = False
                
        for i in range(len(missing)):
            if missing[i]:
                return i+1
            
        return len(nums)+1
        

# alternative solution where we use constant extra space but is slower (although with the same time complexity)
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        nums.append(0)
        leng = len(nums)
        
        for i in range(leng):
            if nums[i] < 0 or nums[i] >= leng:
                nums[i] = 0
                
        for i in range(leng):
            nums[nums[i]%leng] += leng
            
        for i in range(1, leng):
            if nums[i] < leng:
                return i
            
        return leng
        
      
