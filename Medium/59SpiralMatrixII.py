class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        
        ans = [[0 for col in range(n)] for row in range(n)]
        row, col = 0, 0
        direction = 0
        add_row = [0, 1, 0, -1]
        add_col = [1, 0, -1, 0]
        to_fill = 1
        
        for _ in range(n * n):
            ans[row][col] = to_fill
            to_fill += 1
            
            next_r = row + add_row[direction]
            next_c = col + add_col[direction]
            
            if next_r >= 0 and next_c >= 0 and next_r < n and next_c < n and ans[next_r][next_c] == 0:
                row = next_r
                col = next_c
            else:
                direction = (direction + 1) % 4
                row += add_row[direction]
                col += add_col[direction]
                
        return ans
        
