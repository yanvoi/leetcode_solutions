class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        self.ans = []
        self.__get_subsets__(nums, [])
        return self.ans
    
    
    def __get_subsets__(self, nums, curr):
        
        self.ans.append(curr)
        
        for i in range(len(nums)):
            self.__get_subsets__(nums[i+1:], curr + [nums[i]])
        
