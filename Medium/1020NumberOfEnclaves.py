class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:

        self.grid = grid
        self.m, self.n = len(grid), len(grid[0])
        for i in range(self.m):
            for j in range(self.n):
                if self.grid[i][j] and (i == 0 or j == 0 or i == self.m - 1 or j == self.n - 1):
                    self._dfs(i, j)

        return sum(sum(row) for row in self.grid)


    def _dfs(self, i, j):
        self.grid[i][j] = 0
        for k, l in ([-1, 0], [1, 0], [0, -1], [0, 1]):
            x, y = i + k, j + l
            if 0 <= x < self.m and 0 <= y < self.n and self.grid[x][y]:
                self._dfs(x, y)
