class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        self.ans = []
        self.__get_permutations__(nums, [])
        return self.ans
    
    
    def __get_permutations__(self, arr, curr):
        if not arr:
            self.ans.append(curr)
            return
        
        for i in range(len(arr)):
            self.__get_permutations__(arr[:i] + arr[i+1:], curr + [arr[i]])
        
