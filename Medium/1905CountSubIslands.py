class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:

        self.grid1, self.grid2 = grid1, grid2
        return sum(self.dfs(i, j) for i in range(len(grid2)) for j in range(len(grid2[0])) if self.grid2[i][j])

    
    def dfs(self, i, j):

        if not (0 <= i < len(self.grid2) and 0 <= j < len(self.grid2[0]) and self.grid2[i][j] == 1):
            return 1

        self.grid2[i][j] = 0

        ret = self.grid1[i][j]
        up_down = self.dfs(i - 1, j) & self.dfs(i + 1, j)
        left_right = self.dfs(i, j - 1) & self.dfs(i, j + 1)

        return ret & up_down & left_right
