class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        
        prev = float('-inf')
        ans = []
        
        for index, char in enumerate(s):
            if char == c:
                prev = index
            
            ans.append(index - prev)
            
        prev = float('inf')
        for index in range(len(s)-1, -1, -1):
            if s[index] == c:
                prev = index
            ans[index] = min(ans[index], prev - index)
            
        return ans
    
