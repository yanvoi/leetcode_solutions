class Solution:
    def convert(self, s: str, numRows: int) -> str:
        
        if numRows == 1 or numRows >= len(s): return s
        
        ans = [[] for _ in range(numRows)]
        index, step = 0, 1

        for char in s:
            ans[index].append(char)
            if index == numRows - 1:
                step = -1
            elif index == 0:
                step = 1

            index += step

        return ''.join(''.join(row) for row in ans)
        
