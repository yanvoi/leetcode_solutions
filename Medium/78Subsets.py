class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        def backtrack(arr, subset, ans):
            
            ans.append(subset)
            
            for i in range(len(arr)):
                backtrack(arr[i+1:], subset + [arr[i]], ans)
            
        ans = []
        backtrack(nums, [], ans)
        return ans
        
