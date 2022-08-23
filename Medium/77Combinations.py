class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        def backtrack(arr, combination, k, answer):
            if k == 0:
                answer.append(combination)
                return
            
            for i in range(len(arr)):
                backtrack(arr[i+1:], combination + [arr[i]], k-1, answer)
                
        ans = []
        backtrack(list(range(1, n+1)), [], k, ans)
        return ans
        
