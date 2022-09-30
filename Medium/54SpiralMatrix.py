class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        ans = []
        if len(matrix) == 0: return ans
        
        m = len(matrix)
        n = len(matrix[0])
        seen = [[False for col in range(n)] for row in range(m)]
        
        row = 0
        col = 0
        add_r = [0, 1, 0, -1]
        add_c = [1, 0, -1, 0]
        direction = 0
        
        for _ in range(m * n):
            ans.append(matrix[row][col])
            seen[row][col] = True
            
            cr = row + add_r[direction]
            cc = col + add_c[direction]
            
            if cr >= 0 and cc >= 0 and cr < m and cc < n and not seen[cr][cc]:
                row = cr
                col = cc
            else:
                direction = (direction + 1) % 4
                row += add_r[direction]
                col += add_c[direction]
                
        return ans
        
