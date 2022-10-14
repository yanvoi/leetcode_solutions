class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        self.board = [['.'] * n for i in range(n)]
        self.ans = []
        self.solve(0)
        
        return self.ans
        
        
    def solve(self, row):
        
        if row == len(self.board):
            self.ans.append([''.join(r) for r in self.board])
            return True
        
        for j in range(len(self.board)):
            if self.is_valid(row, j):
                self.board[row][j] = 'Q'
                self.solve(row + 1)
                self.board[row][j] = '.'
                
        
    def is_valid(self, i, j):
        
        for sub in range(len(self.board)):
            
            if self.board[sub][j] == 'Q':
                return False
            
            if i - sub >= 0 and j - sub >= 0 and self.board[i-sub][j-sub] == 'Q':
                return False
            
            if i - sub >= 0 and j + sub < len(self.board) and self.board[i-sub][j+sub] == 'Q':
                return False
            
        return True
    
