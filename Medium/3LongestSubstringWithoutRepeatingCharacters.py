class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        used, start, ans = dict(), 0, 0
        
        for i, char in enumerate(s):
            if char in used and used[char] >= start:
                start = used[char] + 1
            else:
                ans = max(ans, i - start + 1)
                
            used[char] = i
            
        return ans
        
