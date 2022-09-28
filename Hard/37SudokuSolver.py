class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        
        self.board = board
        self.solve()
        
        
    def solve(self):
        row, col = self.find_next_empty()

        if row is None:
            return True

        for guess in range(1, 10):
            if self.is_valid(row, col, str(guess)):
                self.board[row][col] = str(guess)
                if self.solve():
                    return True

            self.board[row][col] = '.'

        return False


    def find_next_empty(self):
        for row in range(9):
            for col in range(9):
                if self.board[row][col] == '.':
                    return row, col

        return None, None


    def is_valid(self, row, col, guess):

        if guess in self.board[row]:
            return False

        in_col = [self.board[i][col] for i in range(9)]
        if guess in in_col:
            return False

        r_start = (row // 3) * 3
        c_start = (col // 3) * 3
        for i in range(r_start, r_start + 3):
            for j in range(c_start, c_start + 3):
                if guess == self.board[i][j]:
                    return False

        return True
