class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        
        self.grid = grid
        
        for i in range(len(self.grid)):
            for j in (0, len(self.grid[0]) - 1):
                self.__dfs__(i, j)
                
        for i in (0, len(self.grid) - 1):
            for j in range(len(self.grid[0])):
                self.__dfs__(i, j)
                
        count = 0
        for i in range(1, len(self.grid) - 1):
            for j in range(1, len(self.grid[0]) - 1):
                if self.grid[i][j] == 0:
                    count += 1
                    self.__dfs__(i, j)
                    
        return count
                
        
    
    def __dfs__(self, i, j):
        
        if i < 0 or j < 0 or i >= len(self.grid) or j >= len(self.grid[0]) or self.grid[i][j] > 0:
            return
        
        self.grid[i][j] = 1
        
        self.__dfs__(i-1, j)
        self.__dfs__(i+1, j)
        self.__dfs__(i, j-1)
        self.__dfs__(i, j+1)
        
