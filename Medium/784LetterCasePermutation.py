class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        
        ans = ['']
        
        for char in s:
            
            if char.isalpha():
                ans = [before + ch for before in ans for ch in [char.lower(), char.upper()]]
            else:
                ans = [before + char for before in ans]
                
        return ans
        
