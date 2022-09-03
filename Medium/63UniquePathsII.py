class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        row, col = len(obstacleGrid), len(obstacleGrid[0])
        
        if obstacleGrid[0][0] == 1: return 0
        obstacleGrid[0][0] = 1
        
        for i in range(1, row):
            if obstacleGrid[i][0] == 1:
                obstacleGrid[i][0] = 0
            else:
                obstacleGrid[i][0] = obstacleGrid[i-1][0]
                
        for j in range(1, col):
            if obstacleGrid[0][j] == 1:
                obstacleGrid[0][j] = 0
            else:
                obstacleGrid[0][j] = obstacleGrid[0][j-1]
        
        for i in range(1, row):
            for j in range(1, col):
                if obstacleGrid[i][j] == 0:
                    obstacleGrid[i][j] = obstacleGrid[i-1][j] + obstacleGrid[i][j-1]
                else:
                    obstacleGrid[i][j] = 0
                    
        return obstacleGrid[row - 1][col - 1]
        
