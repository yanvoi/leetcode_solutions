class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        mapping = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        
        def backtrack(numbers, comb, ans):
            if len(numbers) == 0:
                ans.append(comb)
                return
            
            num = numbers[0]
            for dig in mapping[num]:
                backtrack(numbers[1:], comb + dig, ans)
                
                
        if len(digits) == 0: return []
        ans = []
        backtrack(digits, '', ans)
        return ans
        
