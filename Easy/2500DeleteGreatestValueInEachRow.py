class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        for row in grid: row.sort()
        return sum(max(grid[i][j] for i in range(m)) for j in range(n))
