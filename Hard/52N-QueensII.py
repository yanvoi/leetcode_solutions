class Solution:
    def totalNQueens(self, n: int) -> int:
        
        self.count = 0
        # if board[row][col] == 0 it means it's empty
        # if board[row][col] == 1 it means it's not empty
        self.board = [[0] * n for _ in range(n)]
        self.solve(0)
        
        return self.count
    
    
    def solve(self, row):
        
        if row == len(self.board):
            self.count += 1
            return
        
        for j in range(len(self.board)):
            if self.is_valid(row, j):
                self.board[row][j] = 1
                self.solve(row+1)
                self.board[row][j] = 0
        
        
    def is_valid(self, i, j):
        
        for s in range(len(self.board)):
            
            if self.board[s][j]:
                return False
            
            if i - s >= 0 and j - s >= 0 and self.board[i-s][j-s]:
                return False
            
            if i - s >= 0 and j + s < len(self.board) and self.board[i-s][j+s]:
                return False
            
        return True
    
