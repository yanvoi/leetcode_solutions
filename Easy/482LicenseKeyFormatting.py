class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        
        changed = s.replace('-', '').upper()[::-1]
        ans = ''
        
        for i in range(0, len(changed), k):
            ans += changed[i:i+k]
            if i < len(changed) - k:
                ans += '-'
        
        return ans[::-1]
    
