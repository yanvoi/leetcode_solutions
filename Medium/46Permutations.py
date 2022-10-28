class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        self.ans = []
        self.__get_permutations__(nums, [])
        return self.ans
    
    
    def __get_permutations__(self, nums, curr):
        if not nums:
            self.ans.append(curr)
            return
        
        for i in range(len(nums)):
            self.__get_permutations__(nums[:i] + nums[i+1:], curr + [nums[i]])
        
