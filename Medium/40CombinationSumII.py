class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        def backtrack(arr, path, tar, ans):
            
            if tar == 0:
                ans.append(path)
                return
            
            for i in range(len(arr)):
                
                if i > 0 and arr[i] == arr[i-1]:
                    continue
                    
                if arr[i] > tar:
                    break
                    
                backtrack(arr[i+1:], path + [arr[i]], tar - arr[i], ans)
                
                
        candidates.sort()
        ans = []
        backtrack(candidates, [], target, ans)
        
        return ans
        
