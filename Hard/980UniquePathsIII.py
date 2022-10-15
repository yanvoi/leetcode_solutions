class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        
        self.grid = grid
        self.answer = 0
        i, j = 0, 0
        # we have to initialize it as 1 because the starting square
        # will not be counted when we go over the array
        empty = 1
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    i, j = row, col
                elif grid[row][col] == 0:
                    empty += 1
                    
        self.dfs(i, j, empty)
        return self.answer
        
        
    def dfs(self, i, j, empty):
        
        # when we go out of bounds of the array or if we meet an obstacle, we have to return
        if i < 0 or j < 0 or i >= len(self.grid) or j >= len(self.grid[0]) or self.grid[i][j] < 0:
            return
        
        # when we walk over the ending square and have walked over all non-obstacle squares
        # we increment the answer value and return from the call
        if self.grid[i][j] == 2:
            if empty == 0: self.answer += 1
            return
        
        self.grid[i][j] -= 2
        
        self.dfs(i - 1, j, empty - 1)
        self.dfs(i + 1, j, empty - 1)
        self.dfs(i, j - 1, empty - 1)
        self.dfs(i, j + 1, empty - 1)
        
        self.grid[i][j] = 0
        
