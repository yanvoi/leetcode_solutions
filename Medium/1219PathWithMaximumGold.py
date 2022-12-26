class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        
        self.grid = grid
        ans = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                ans = max(ans, self.__dfs__(i, j))
                
        return ans
        
        
    def __dfs__(self, i, j):
        
        if i < 0 or j < 0 or i >= len(self.grid) or j >= len(self.grid[0]) or self.grid[i][j] == 0:
            return 0
        
        tmp = self.grid[i][j]
        self.grid[i][j] = 0

        up_down = max(self.__dfs__(i-1, j), self.__dfs__(i+1, j))
        left_right = max(self.__dfs__(i, j-1), self.__dfs__(i, j+1))

        self.grid[i][j] = tmp
        return tmp + max(up_down, left_right)
        
