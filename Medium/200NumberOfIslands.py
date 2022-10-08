class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    count += 1
                    self.__clean__(grid, i, j)
                    
        return count
                    
                    
    def __clean__(self, grid, i, j):
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != '1':
            return
        
        grid[i][j] = '#'
        
        self.__clean__(grid, i-1, j)
        self.__clean__(grid, i+1, j)
        self.__clean__(grid, i, j-1)
        self.__clean__(grid, i, j+1)
        
