class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        
        ans = 0
        for s in strs:
            val = int(s) if s.isnumeric() else len(s)
            ans = max(ans, val)
            
        return ans
        
