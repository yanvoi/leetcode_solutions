class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:

        row = [0 for _ in range(len(grid))]
        col = [0 for _ in range(len(grid[0]))]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                row[i] += grid[i][j]
                col[j] += grid[i][j]

        diff = [[0 for j in range(len(grid[0]))] for i in range(len(grid))]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                diff[i][j] = row[i] + col[j] - (len(grid) - row[i]) - (len(grid[0]) - col[j])

        return diff
