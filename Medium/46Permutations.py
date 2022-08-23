class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        def backtrack(arr, permutation, ans):
            
            if not arr:
                ans.append(permutation)
                return
            
            for i in range(len(arr)):
                backtrack(arr[:i] + arr[i+1:], permutation + [arr[i]], ans)
                
        ans = []
        backtrack(nums, [], ans)
        return ans
        
