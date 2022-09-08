class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        copied_grid = grid.copy()
        self.answer = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    self.curr_size = 0
                    self.__backtrackIsland__(copied_grid, i, j)
                    self.answer = max(self.answer, self.curr_size)
        
        return self.answer
    
    def __backtrackIsland__(self, arr, i, j):
        if i < 0 or i >= len(arr) or j < 0 or j >= len(arr[0]) or arr[i][j] == 0: return
        
        self.curr_size += 1
            
        arr[i][j] = 0
        self.__backtrackIsland__(arr, i-1, j)
        self.__backtrackIsland__(arr, i+1, j)
        self.__backtrackIsland__(arr, i, j-1)
        self.__backtrackIsland__(arr, i, j+1)
        
