class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        def backtrack(arr, path, answer):
            
            if len(arr) == 0:
                answer.append(path)
                return
            
            for i in range(len(arr)):
                
                if i > 0 and arr[i] == arr[i-1]:
                    continue
                    
                backtrack(arr[:i] + arr[i+1:], path + [arr[i]], answer)
            
        
        nums.sort()
        ans = []
        backtrack(nums, [], ans)
        return ans
        
