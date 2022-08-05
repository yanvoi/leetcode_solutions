class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        
        s = set()
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    s.add((i, j))
                    
        for row, col in s:
            for j in range(len(matrix[row])):
                matrix[row][j] = 0
            for i in range(len(matrix)):
                matrix[i][col] = 0
        
