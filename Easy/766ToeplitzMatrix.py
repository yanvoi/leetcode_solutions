class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        
        for i in range(len(matrix)):
            
            val = matrix[i][0]
            x = i + 1
            y = 1
            
            while x < len(matrix) and y < len(matrix[0]):
                if matrix[x][y] != val:
                    return False
                x += 1
                y += 1
                
        for i in range(len(matrix[0])):
            
            val = matrix[0][i]
            x = 1
            y = i + 1
            
            while x < len(matrix) and y < len(matrix[0]):
                if matrix[x][y] != val:
                    return False
                x += 1
                y += 1
            
        return True
        
