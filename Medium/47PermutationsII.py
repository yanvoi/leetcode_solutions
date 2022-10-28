class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        self.ans = []
        self.__permute__(nums, [])
        return self.ans
    
    
    def __permute__(self, nums, curr):
        
        if not nums:
            self.ans.append(curr)
            return
        
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
                
            self.__permute__(nums[:i] + nums[i+1:], curr + [nums[i]])
        
