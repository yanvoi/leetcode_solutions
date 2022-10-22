class Solution:
    def solve(self, board: List[List[str]]) -> None:
        
        self.board = board
        
        # marking all non surrounded regions as 'T'
        # a non surrounded region connects or semi connects to an 'O' on a border
        for i in range(len(board)):
            for j in [0, len(board[0]) - 1]:
                self.__dfs__(i, j)
                
        # same here
        for i in [0, len(board) - 1]:
            for j in range(len(board[0])):
                self.__dfs__(i, j)
                
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.board[i][j] == 'T':
                    self.board[i][j] = 'O'
                else:
                    self.board[i][j] = 'X'
                
        return self.board
    
    
    def __dfs__(self, i, j):
        
        if i < 0 or j < 0 or i >= len(self.board) or j >= len(self.board[0]):
            return
        
        if self.board[i][j] != 'O':
            return
        
        self.board[i][j] = 'T'
        self.__dfs__(i-1, j)
        self.__dfs__(i+1, j)
        self.__dfs__(i, j-1)
        self.__dfs__(i, j+1)
        
