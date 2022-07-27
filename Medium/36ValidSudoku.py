class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for row in board:
            s = set()
            for el in row:
                if el != '.' and el in s:
                    return False
                s.add(el)
                
        for i in range(len(board)):
            s = set()
            for j in range(len(board)):
                if board[j][i] != '.' and board[j][i] in s:
                    return False
                s.add(board[j][i])
                
        k = 0
        while k < 9:
            l = 0
            while l < 9:
                s = set()
                for i in range(3):
                    for j in range(3):
                        if board[k + i][l + j] != '.' and board[k + i][l + j] in s:
                            return False
                        s.add(board[k + i][l + j])
                l += 3
            k += 3
        
        return True
    
