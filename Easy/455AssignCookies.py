class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        
        ans = 0
        g.sort()
        s.sort()
        
        k = len(g) - 1
        
        while s and k >= 0:
            cookie = s.pop()
            
            while k >= 0 and cookie < g[k]:
                k -= 1
                
            if k >= 0: ans += 1
            k -= 1
            
        return ans
        
