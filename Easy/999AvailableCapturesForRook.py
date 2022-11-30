class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        
        ans = 0
        x, y = next((i, j) for i in range(8) for j in range(8) if board[i][j] == 'R')
                    
        i = x - 1
        while i >= 0 and board[i][y] != 'B':
            if board[i][y] == 'p':
                ans += 1
                break
            i -= 1
                
        i = x + 1
        while i < 8 and board[i][y] != 'B':
            if board[i][y] == 'p':
                ans += 1
                break
            i += 1
            
        j = y - 1
        while j >= 0 and board[x][j] != 'B':
            if board[x][j] == 'p':
                ans += 1
                break
            j -= 1
        
        j = y + 1
        while j < 8 and board[x][j] != 'B':
            if board[x][j] == 'p':
                ans += 1
                break
            j += 1
        
        return ans
        
