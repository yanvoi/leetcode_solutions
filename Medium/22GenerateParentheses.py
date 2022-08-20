class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        def backtracking(path, left, right, ans):
            
            if len(path) == 2 * n:
                ans.append(''.join(path))
                return
            
            if left < n:
                path.append('(')
                backtracking(path, left+1, right, ans)
                path.pop()
                
            if right < left:
                path.append(')')
                backtracking(path, left, right+1, ans)
                path.pop()
    
        ans = []
        backtracking([], 0, 0, ans)
        return ans
    
