class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        
        ans = 0
        
        for i in range(len(grid) - 2):
            for j in range(len(grid[0]) - 2):
                cur = 0
                
                for y in range(j, j+3):
                    cur += grid[i][y]
                    
                for y in range(j, j+3):
                    cur += grid[i+2][y]
                    
                cur += grid[i+1][j+1]
                
                ans = max(ans, cur)
                
        return ans
        
