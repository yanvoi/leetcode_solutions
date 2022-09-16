class Solution:
    def convert(self, s: str, numRows: int) -> str:
        
        if numRows <= 1: return s
            
        curRow, step = 0, 1
        ans = [''] * numRows
        
        for char in s:
            
            ans[curRow] += char
            
            if curRow == numRows - 1:
                step = -1
            elif curRow == 0:
                step = 1
                
            curRow += step
            
        return ''.join(ans)
        
