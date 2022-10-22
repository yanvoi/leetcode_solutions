class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        # USING SLIDING WINDOW TECHNIQUE
        
        if not s or not t or len(t) > len(s): return ''
        
        # ans == (windows size, left pointer, right pointer)
        ans = (-1, 0, 0)
        
        # 'formed' is gonna count many unique letters we have formed
        # in our current window
        left, right, formed = 0, 0, 0
        needed = dict()
        for char in t:
            needed[char] = needed.get(char, 0) + 1
        
        # holds the frequency of letters of the current window
        window = dict()
        
        while right < len(s):
            
            char = s[right]
            window[char] = window.get(char, 0) + 1
            
            if char in needed and window[char] == needed[char]:
                formed += 1
                
            while left <= right and formed == len(needed):
                
                # we only change ans if the current window is shorter
                # or if the answer doesn't exist yet
                if right - left + 1 < ans[0] or ans[0] == -1:
                    ans = (right - left + 1, left, right)
                    
                # making the window shorter and checking if it works or not
                char = s[left]
                window[char] -= 1
                
                if char in needed and needed[char] > window[char]:
                    formed -= 1
                    
                left += 1
                
            right += 1
            
        return '' if ans[0] == -1 else s[ans[1]:ans[2]+1]
        
