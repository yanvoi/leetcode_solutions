class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        
        def delete_ship(matrix, i, j):
            matrix[i][j] = '.'
            
            row = i - 1
            while row >= 0 and matrix[row][j] == 'X':
                matrix[row][j] = '.'
                row -= 1
                
            row = i + 1
            while row < len(matrix) and matrix[row][j] == 'X':
                matrix[row][j] = '.'
                row += 1
                
            col = j - 1
            while col >= 0 and matrix[i][col] == 'X':
                matrix[i][col] = '.'
                col -= 1
                
            col = j + 1
            while col < len(matrix[0]) and matrix[i][col] == 'X':
                matrix[i][col] = '.'
                col += 1
        
        ans = 0
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'X':
                    ans += 1
                    delete_ship(board, i, j)
        
        return ans
        
