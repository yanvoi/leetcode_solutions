class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        
        ans = 0
        
        # from the top and the side
        for i in range(len(grid)):
            biggest = 0
            for j in range(len(grid[0])):
                biggest = max(biggest, grid[i][j])
                if grid[i][j] != 0:
                    ans += 1
            ans += biggest
                    
        # from the front
        for j in range(len(grid[0])):
            biggest = 0
            for i in range(len(grid)):
                biggest = max(biggest, grid[i][j])
            ans += biggest
            
        return ans
        
