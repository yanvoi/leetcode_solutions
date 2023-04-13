class Solution:
    def minPathCost(self, grid: List[List[int]], moveCost: List[List[int]]) -> int:

        m, n = len(grid), len(grid[0])
        dp = [[inf if i else grid[i][j] for j in range(n)] for i in range(m)]
        
        for row in range(1, m):
            for col in range(n):
                for prev_col in range(n):
                    prev_dp = dp[row - 1][prev_col]
                    prev_val = grid[row - 1][prev_col]
                    
                    possible_new_dp = prev_dp + grid[row][col] + moveCost[prev_val][col]
                    dp[row][col] = min(dp[row][col], possible_new_dp)
        
        return min(dp[-1])
