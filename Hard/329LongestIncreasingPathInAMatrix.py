class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        
        if not matrix or not matrix[0]: return 0
        self.matrix = matrix
        self.M, self.N = len(matrix), len(matrix[0])
        self.arr = [[0] * self.N for i in range(self.M)]
        
        return max(self.__dfs__(i, j) for i in range(self.M) for j in range(self.N))
    
    def __dfs__(self, i, j):
        
        if not self.arr[i][j]:
            val = self.matrix[i][j]
            self.arr[i][j] = 1 + max(self.__dfs__(i-1, j) if i and self.matrix[i-1][j] < val else 0,
                                     self.__dfs__(i+1, j) if i < self.M - 1 and self.matrix[i+1][j] < val else 0,
                                     self.__dfs__(i, j-1) if j and self.matrix[i][j-1] < val else 0,
                                     self.__dfs__(i, j+1) if j < self.N - 1 and self.matrix[i][j+1] < val else 0)
        
        return self.arr[i][j]
    
